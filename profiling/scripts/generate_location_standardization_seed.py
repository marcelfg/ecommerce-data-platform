"""
Generate dbt/seeds/location_standardization.csv by running the same four-tier
classification as profiling/scripts/compare_city_names.py, then mapping each
distinct (raw_city, raw_state) pair to its official standardised form.

Tiers (in order):
  1. Município  — exact normalised match against IBGE municipalities
  2. Distrito   — exact normalised match against IBGE districts
  3. Fuzzy      — SequenceMatcher ≥ 0.85 against município list, same state
  4. ViaCEP     — zip-prefix lookup via https://viacep.com.br
  5. Manual     — hardcoded corrections + DF administrative region rule

All five sections are included in the seed, including municipio/distrito matches,
because the raw staging value (lowercase, no accents) differs from the official
IBGE form and still needs a mapping row.

Usage:
    uv run standardization/generate_location_standardization_seed.py           # write seed
    uv run standardization/generate_location_standardization_seed.py --preview  # print sample only
"""

import argparse
import csv
import difflib
import gzip
import json
import re
import time
import unicodedata
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

import pandas as pd

# ---------------------------------------------------------------------------
# Paths & constants
# ---------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).parent.parent.parent
DATA_DIR = PROJECT_ROOT / "data"
SEED_PATH = PROJECT_ROOT / "dbt" / "seeds" / "location_standardization.csv"

IBGE_MUNICIPIOS_URL = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios"
IBGE_DISTRITOS_URL = "https://servicodados.ibge.gov.br/api/v1/localidades/distritos"
VIACEP_URL = "https://viacep.com.br/ws/{cep}/json/"

FUZZY_THRESHOLD = 0.85
VIACEP_DELAY = 0.2  # seconds between requests

SOURCES: dict[str, tuple[str, str, str]] = {
    "customers": ("olist_customers_dataset.csv", "customer_city", "customer_state"),
    "sellers": ("olist_sellers_dataset.csv", "seller_city", "seller_state"),
    "geolocation": ("olist_geolocation_dataset.csv", "geolocation_city", "geolocation_state"),
}

ZIP_COL: dict[str, str] = {
    "customers": "customer_zip_code_prefix",
    "sellers": "seller_zip_code_prefix",
    "geolocation": "geolocation_zip_code_prefix",
}

# ---------------------------------------------------------------------------
# Manual corrections (Section 5 — no confident match)
# Keyed by (normalize(raw_city), normalize(raw_state)) so that accented variants
# of the same city resolve to the same correction without duplicate entries.
# ---------------------------------------------------------------------------

# fmt: off
_MANUAL_RAW: list[tuple[str, str, str, str]] = [
    # raw_city,                                     raw_state, std_city,                    std_state
    ("primavera",                                    "SP",      "Rosana",                    "SP"),
    ("japuiba",                                      "RJ",      "Cachoeiras de Macacu",      "RJ"),
    ("japuíba",                                      "RJ",      "Cachoeiras de Macacu",      "RJ"),
    ("catu de abrantes",                             "BA",      "Camaçari",                  "BA"),
    ("buzios",                                       "RJ",      "Armação dos Búzios",        "RJ"),
    ("búzios",                                       "RJ",      "Armação dos Búzios",        "RJ"),
    ("ilha grande",                                  "RJ",      "Angra dos Reis",            "RJ"),
    ("piabeta",                                      "RJ",      "Magé",                      "RJ"),
    ("planaltina de goias",                          "GO",      "Planaltina",                "GO"),
    ("boa esperanca",                                "MT",      "Boa Esperança do Norte",    "MT"),
    ("boa esperança",                                "MT",      "Boa Esperança do Norte",    "MT"),
    ("arembepe",                                     "BA",      "Camaçari",                  "BA"),
    ("luziapolis",                                   "AL",      "Campo Alegre",              "AL"),
    ("pau d'arco",                                   "AL",      "Arapiraca",                 "AL"),
    ("vila sao francisco",                           "AL",      "Arapiraca",                 "AL"),
    ("jaua",                                         "BA",      "Camaçari",                  "BA"),
    ("aguas claras df",                              "SP",      "Brasília",                  "DF"),
    ("andira-pr",                                    "PR",      "Barra do Jacaré",           "PR"),
    ("andradas",                                     "SP",      "Andradas",                  "MG"),
    ("bahia",                                        "BA",      "Paulo Afonso",              "BA"),
    ("barbacena/ minas gerais",                      "MG",      "Barbacena",                 "MG"),
    ("castro pires",                                 "MG",      "Teófilo Otoni",             "MG"),
    ("centro",                                       "MG",      "Pará de Minas",             "MG"),
    ("marechal candido rondon",                      "PA",      "Marechal Cândido Rondon",   "PR"),
    ("marechal candido rondon",                      "SP",      "Marechal Cândido Rondon",   "PR"),
    ("novo hamburgo, rio grande do sul, brasil",     "RS",      "Novo Hamburgo",             "RS"),
    ("rio de janeiro \\rio de janeiro",              "RJ",      "Rio de Janeiro",            "RJ"),
    ("vila velha",                                   "SP",      "Vila Velha",                "ES"),
    ("volta redonda",                                "SP",      "Volta Redonda",             "RJ"),
    ("bacaxa (saquarema) - distrito",                "RJ",      "Saquarema",                 "RJ"),
    ("california da barra (barra do pirai)",         "RJ",      "Barra do Piraí",            "RJ"),
    ("coqueiral",                                    "ES",      "Aracruz",                   "ES"),
    ("jacare (cabreuva)",                            "SP",      "Cabreúva",                  "SP"),
    ("jacaré (cabreúva)",                            "SP",      "Cabreúva",                  "SP"),
    ("macuco",                                       "MG",      "Muriaé",                    "MG"),
    ("monte gordo (camacari) - distrito",            "BA",      "Camaçari",                  "BA"),
    ("nova andradina",                               "RS",      "Nova Andradina",            "MS"),
    ("nova redencao bahia",                          "BA",      "Nova Redenção",             "BA"),
    ("realeza (manhuacu)",                           "MG",      "Manhuaçu",                  "MG"),
    ("são joão do pau d%26apos%3balho",              "SP",      "São João do Pau D'Alho",    "SP"),
    ("tamoios (cabo frio)",                          "RJ",      "Cabo Frio",                 "RJ"),
]
# fmt: on


def _build_manual_corrections() -> dict[tuple[str, str], tuple[str, str]]:
    """
    Build a normalized-key lookup for manual corrections.

    Keyed by (normalize(raw_city), normalize(raw_state)) so accented and
    unaccented variants of the same city resolve to the same correction.
    """
    corrections: dict[tuple[str, str], tuple[str, str]] = {}
    for raw_city, raw_state, std_city, std_state in _MANUAL_RAW:
        key = (normalize(raw_city), normalize(raw_state))
        corrections[key] = (std_city, std_state)
    return corrections


# ---------------------------------------------------------------------------
# Staging simulation  (mirrors staging models)
# ---------------------------------------------------------------------------


def stage_city(s: str) -> str:
    """Simulate Snowflake LOWER(TRIM(city))."""
    return s.lower().strip()


def stage_state(s: str) -> str:
    """Simulate Snowflake UPPER(TRIM(state))."""
    return s.upper().strip()


# ---------------------------------------------------------------------------
# Normalisation  (used for matching only, never written to the seed)
# ---------------------------------------------------------------------------


def normalize(s: str) -> str:
    """
    Normalise a string for comparison.

    Steps: lowercase → strip diacritics (NFKD) → remove all whitespace.
    """
    s = s.lower()
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")
    s = re.sub(r"\s+", "", s)
    return s


# ---------------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------------


def _fetch_json(url: str, timeout: int = 60) -> list | dict:
    """Fetch JSON from a URL, handling gzip compression transparently."""
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        raw = resp.read()
    try:
        raw = gzip.decompress(raw)
    except (OSError, gzip.BadGzipFile):
        pass
    return json.loads(raw.decode("utf-8"))


# ---------------------------------------------------------------------------
# IBGE fetching
# ---------------------------------------------------------------------------


def _extract_state_sigla(item: dict) -> str | None:
    """Extract state abbreviation from an IBGE município dict (two path fallbacks)."""
    try:
        return item["microrregiao"]["mesorregiao"]["UF"]["sigla"]
    except (TypeError, KeyError):
        pass
    try:
        return item["regiao-imediata"]["regiao-intermediaria"]["UF"]["sigla"]
    except (TypeError, KeyError):
        pass
    return None


def fetch_ibge_municipios() -> list[dict[str, str]]:
    """
    Fetch all Brazilian municipalities from the IBGE API.

    Returns a list of dicts with keys 'nome' and 'sigla'.
    """
    print(f"  Fetching municipalities …")
    data: list[dict] = _fetch_json(IBGE_MUNICIPIOS_URL)
    result, skipped = [], 0
    for item in data:
        sigla = _extract_state_sigla(item)
        if sigla is None:
            skipped += 1
            continue
        result.append({"nome": item["nome"], "sigla": sigla})
    if skipped:
        print(f"  Warning: {skipped} município entries skipped")
    print(f"  {len(result)} municipalities loaded")
    return result


def fetch_ibge_distritos() -> list[dict[str, str]]:
    """
    Fetch all Brazilian districts from the IBGE API.

    Returns a list of dicts with keys 'nome', 'municipio_nome', and 'sigla'.
    'municipio_nome' is the parent municipality name — used as standardized_city so
    district entries map to their parent city, not to the district name itself.
    """
    print(f"  Fetching districts …")
    data: list[dict] = _fetch_json(IBGE_DISTRITOS_URL)
    result, skipped = [], 0
    for item in data:
        try:
            sigla = _extract_state_sigla(item["municipio"])
            if sigla is None:
                raise ValueError
            result.append({
                "nome": item["nome"],
                "municipio_nome": item["municipio"]["nome"],
                "sigla": sigla,
            })
        except (TypeError, KeyError, ValueError):
            skipped += 1
    if skipped:
        print(f"  Warning: {skipped} distrito entries skipped")
    print(f"  {len(result)} districts loaded")
    return result


# ---------------------------------------------------------------------------
# CSV loading
# ---------------------------------------------------------------------------


def load_pair_counts() -> dict[tuple[str, str], dict[str, int]]:
    """
    Count raw row occurrences of each (staged_city, staged_state) pair per source.

    Returns {(city, state): {source_name: count}}.
    """
    all_counts: dict[tuple[str, str], dict[str, int]] = defaultdict(dict)
    for source_name, (csv_file, city_col, state_col) in SOURCES.items():
        df = pd.read_csv(DATA_DIR / csv_file, usecols=[city_col, state_col], dtype=str).dropna(
            subset=[city_col, state_col]
        )
        df["_city"] = df[city_col].map(stage_city)
        df["_state"] = df[state_col].map(stage_state)
        for (city, state), count in df.groupby(["_city", "_state"]).size().items():
            all_counts[(city, state)][source_name] = int(count)
    return all_counts


def load_zip_for_pairs() -> dict[tuple[str, str], Counter]:
    """
    For each (staged_city, staged_state) pair, collect all associated zip code prefixes.

    Zip prefixes are zero-padded to 5 digits.
    Returns {(city, state): Counter of zip prefix strings}.
    """
    pair_to_zips: dict[tuple[str, str], Counter] = defaultdict(Counter)
    for source_name, (csv_file, city_col, state_col) in SOURCES.items():
        zip_col = ZIP_COL[source_name]
        df = pd.read_csv(DATA_DIR / csv_file, usecols=[city_col, state_col, zip_col]).dropna(
            subset=[city_col, state_col, zip_col]
        )
        df["_city"] = df[city_col].astype(str).map(stage_city)
        df["_state"] = df[state_col].astype(str).map(stage_state)
        df["_zip"] = df[zip_col].astype(int).apply(lambda z: str(z).zfill(5))
        for (city, state, zp), count in df.groupby(["_city", "_state", "_zip"]).size().items():
            pair_to_zips[(city, state)][zp] += int(count)
    return pair_to_zips


# ---------------------------------------------------------------------------
# Fuzzy matching
# ---------------------------------------------------------------------------


def best_fuzzy_match(
    norm_city: str,
    norm_state: str,
    municipio_by_norm_state: dict[str, list[tuple[str, str]]],
) -> tuple[str | None, float]:
    """
    Return (original_IBGE_nome, score) if the best same-state candidate scores
    ≥ FUZZY_THRESHOLD, else (None, best_score).
    """
    candidates = municipio_by_norm_state.get(norm_state, [])
    best_score, best_name = 0.0, None
    for norm_cand, orig_name in candidates:
        score = difflib.SequenceMatcher(None, norm_city, norm_cand).ratio()
        if score > best_score:
            best_score, best_name = score, orig_name
    if best_score >= FUZZY_THRESHOLD:
        return best_name, best_score
    return None, best_score


# ---------------------------------------------------------------------------
# ViaCEP lookup
# ---------------------------------------------------------------------------


def query_viacep(zip_prefix: str) -> dict | None:
    """
    Query ViaCEP for a 5-digit zip prefix (padded with '000').

    Returns the response dict if valid, else None.
    """
    cep = zip_prefix + "000"
    try:
        data = _fetch_json(VIACEP_URL.format(cep=cep), timeout=10)
        if isinstance(data, dict) and "erro" not in data and "localidade" in data:
            return data
    except Exception:
        pass
    return None


# ---------------------------------------------------------------------------
# Main classification
# ---------------------------------------------------------------------------


def build_seed_rows(preview: bool = False) -> list[dict]:
    """
    Run the four-tier classification and return one dict per (raw_city, raw_state) pair.

    Each dict has keys: raw_city, raw_state, standardized_city, standardized_state, match_method.
    """
    print("\nFetching IBGE reference data …")
    municipios = fetch_ibge_municipios()
    distritos = fetch_ibge_distritos()

    # Build normalised lookup maps
    municipio_norm_to_official: dict[tuple[str, str], tuple[str, str]] = {}
    municipio_by_norm_state: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for m in municipios:
        nc, ns = normalize(m["nome"]), normalize(m["sigla"])
        municipio_norm_to_official[(nc, ns)] = (m["nome"], m["sigla"])
        municipio_by_norm_state[ns].append((nc, m["nome"]))

    distrito_norm_to_official: dict[tuple[str, str], tuple[str, str]] = {}
    for d in distritos:
        nc, ns = normalize(d["nome"]), normalize(d["sigla"])
        if (nc, ns) not in distrito_norm_to_official:
            # Map to the parent municipality, not the district name itself
            distrito_norm_to_official[(nc, ns)] = (d["municipio_nome"], d["sigla"])

    manual_corrections = _build_manual_corrections()

    print("\nLoading source CSVs …")
    all_pair_counts = load_pair_counts()
    print(f"  {len(all_pair_counts)} distinct (city, state) pairs")

    print("\nLoading zip code associations …")
    pair_to_zips = load_zip_for_pairs()

    # ---------- classification ----------
    seed_rows: list[dict] = []
    pending_viacep: list[tuple[str, str]] = []

    for (city, state) in all_pair_counts:
        nc, ns = normalize(city), normalize(state)

        # Tier 1: município
        if (nc, ns) in municipio_norm_to_official:
            std_city, std_state = municipio_norm_to_official[(nc, ns)]
            seed_rows.append({
                "raw_city": city, "raw_state": state,
                "standardized_city": std_city, "standardized_state": std_state,
                "match_method": "municipio",
            })
            continue

        # Tier 2: distrito
        if (nc, ns) in distrito_norm_to_official:
            std_city, std_state = distrito_norm_to_official[(nc, ns)]
            seed_rows.append({
                "raw_city": city, "raw_state": state,
                "standardized_city": std_city, "standardized_state": std_state,
                "match_method": "distrito",
            })
            continue

        # Tier 3: fuzzy
        suggestion, _ = best_fuzzy_match(nc, ns, municipio_by_norm_state)
        if suggestion is not None:
            seed_rows.append({
                "raw_city": city, "raw_state": state,
                "standardized_city": suggestion, "standardized_state": state,
                "match_method": "fuzzy",
            })
            continue

        # Tier 4: ViaCEP (deferred — collected first, queried in bulk below)
        pending_viacep.append((city, state))

    # ---------- ViaCEP bulk lookup ----------
    print(f"\nQuerying ViaCEP for {len(pending_viacep)} unresolved pairs …")
    if preview and len(pending_viacep) > 10:
        print("  (preview mode: querying all to ensure accurate counts)")

    still_unresolved: list[tuple[str, str]] = []
    for i, (city, state) in enumerate(pending_viacep, start=1):
        zip_counter = pair_to_zips.get((city, state), Counter())
        viacep_result = None
        if zip_counter:
            zip_prefix = zip_counter.most_common(1)[0][0]
            viacep_result = query_viacep(zip_prefix)
            time.sleep(VIACEP_DELAY)

        if viacep_result:
            seed_rows.append({
                "raw_city": city, "raw_state": state,
                "standardized_city": viacep_result["localidade"],
                "standardized_state": viacep_result["uf"],
                "match_method": "viacep",
            })
        else:
            still_unresolved.append((city, state))

        if i % 25 == 0 or i == len(pending_viacep):
            print(f"  {i}/{len(pending_viacep)} queried …")

    # ---------- Manual / DF rule ----------
    print(f"\nApplying manual corrections to {len(still_unresolved)} remaining pairs …")
    for city, state in still_unresolved:
        nc, ns = normalize(city), normalize(state)

        # Manual corrections (normalized-key lookup)
        if (nc, ns) in manual_corrections:
            std_city, std_state = manual_corrections[(nc, ns)]
            seed_rows.append({
                "raw_city": city, "raw_state": state,
                "standardized_city": std_city, "standardized_state": std_state,
                "match_method": "manual_review",
            })
            continue

        # DF administrative regions → Brasília
        if state == "DF":
            seed_rows.append({
                "raw_city": city, "raw_state": state,
                "standardized_city": "Brasília", "standardized_state": "DF",
                "match_method": "manual_review",
            })
            continue

        # Fallback: no correction found — keep raw values, flag for review
        print(f"  WARNING: no correction found for ({city!r}, {state!r}) — using raw values")
        seed_rows.append({
            "raw_city": city, "raw_state": state,
            "standardized_city": city, "standardized_state": state,
            "match_method": "manual_review",
        })

    # Sort for stable output
    seed_rows.sort(key=lambda r: (r["raw_state"], r["raw_city"]))
    return seed_rows


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main() -> None:
    """Parse arguments and run the seed generator."""
    parser = argparse.ArgumentParser(description="Generate location_standardization.csv")
    parser.add_argument(
        "--preview",
        action="store_true",
        help="Print a sample and count breakdown without writing the seed file.",
    )
    args = parser.parse_args()

    rows = build_seed_rows(preview=args.preview)

    # Count by method
    from collections import Counter as _Counter
    method_counts = _Counter(r["match_method"] for r in rows)

    print("\n--- Row counts by match_method ---")
    for method in ("municipio", "distrito", "fuzzy", "viacep", "manual_review"):
        print(f"  {method:<16} {method_counts.get(method, 0):>6}")
    print(f"  {'TOTAL':<16} {len(rows):>6}")

    print("\n--- Sample (first 20 rows, sorted by state then city) ---")
    headers = ["raw_city", "raw_state", "standardized_city", "standardized_state", "match_method"]
    col_widths = [max(len(h), max((len(str(r[h])) for r in rows[:20]), default=0)) for h in headers]
    fmt = "  " + "  ".join(f"{{:<{w}}}" for w in col_widths)
    print(fmt.format(*headers))
    print("  " + "  ".join("-" * w for w in col_widths))
    for row in rows[:20]:
        print(fmt.format(*[str(row[h]) for h in headers]))

    if args.preview:
        print(f"\n[preview mode] Seed NOT written. Run without --preview to write {SEED_PATH.relative_to(PROJECT_ROOT)}.")
        return

    SEED_PATH.parent.mkdir(parents=True, exist_ok=True)
    with SEED_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nSeed written → {SEED_PATH.relative_to(PROJECT_ROOT)}  ({len(rows)} rows)")


if __name__ == "__main__":
    main()
