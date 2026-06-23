"""
Compare distinct (city, state) pairs from the three Olist source CSVs against the
official IBGE administrative boundaries. Uses a four-tier validation approach:

  Tier 1 — Município (municipality): exact normalised match against
            https://servicodados.ibge.gov.br/api/v1/localidades/municipios
  Tier 2 — Distrito (district): exact normalised match against
            https://servicodados.ibge.gov.br/api/v1/localidades/distritos
  Tier 3 — Fuzzy matching: SequenceMatcher against the município list within the
            same state; pairs with similarity ≥ FUZZY_THRESHOLD get a suggestion.
  Tier 4 — ViaCEP lookup: for pairs still unresolved after tiers 1–3, the most
            common zip code associated with that (city, state) pair is used to
            query https://viacep.com.br/ws/{cep}/json/ (5-digit prefix + "000").

Report sections
---------------
1. Matched at município level   — no action needed
2. Matched at distrito level    — valid, but a smaller administrative unit
3. Fuzzy suggestion available   — probable typo / spelling variant; correction proposed
4. Matched via ViaCEP           — resolved through zip code lookup; official name recorded
5. No confident match           — unresolved after all four tiers; manual review required

Usage:
    uv run profiling/scripts/compare_city_names.py
"""

import difflib
import gzip
import json
import re
import time
import unicodedata
import urllib.request
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

import pandas as pd

# ---------------------------------------------------------------------------
# Paths & constants
# ---------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).parent.parent.parent
DATA_DIR = PROJECT_ROOT / "data"
REPORT_PATH = PROJECT_ROOT / "profiling" / "reports" / "city_name_mismatches.md"

IBGE_MUNICIPIOS_URL = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios"
IBGE_DISTRITOS_URL = "https://servicodados.ibge.gov.br/api/v1/localidades/distritos"
VIACEP_URL = "https://viacep.com.br/ws/{cep}/json/"
FUZZY_THRESHOLD = 0.85
VIACEP_DELAY = 0.2  # seconds between ViaCEP requests

SOURCES: dict[str, tuple[str, str, str]] = {
    "customers": ("olist_customers_dataset.csv", "customer_city", "customer_state"),
    "sellers": ("olist_sellers_dataset.csv", "seller_city", "seller_state"),
    "geolocation": ("olist_geolocation_dataset.csv", "geolocation_city", "geolocation_state"),
}

# Raw zip-code column for each source file (stored as int64, needs zero-padding)
ZIP_COL: dict[str, str] = {
    "customers": "customer_zip_code_prefix",
    "sellers": "seller_zip_code_prefix",
    "geolocation": "geolocation_zip_code_prefix",
}

# ---------------------------------------------------------------------------
# Staging simulation
# ---------------------------------------------------------------------------


def stage_city(s: str) -> str:
    """Simulate Snowflake LOWER(TRIM(city))."""
    return s.lower().strip()


def stage_state(s: str) -> str:
    """Simulate Snowflake UPPER(TRIM(state))."""
    return s.upper().strip()


# ---------------------------------------------------------------------------
# Normalisation (used only for matching, not for display)
# ---------------------------------------------------------------------------


def normalize(s: str) -> str:
    """
    Normalise a string for comparison.

    Steps: lowercase → strip diacritics via NFKD → remove all whitespace.
    Applied identically to IBGE values and CSV values before matching.
    """
    s = s.lower()
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")
    s = re.sub(r"\s+", "", s)
    return s


# ---------------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------------


def _fetch_json(url: str, timeout: int = 60) -> list | dict:
    """
    Fetch a JSON response from a URL.

    Handles gzip-compressed responses transparently.
    Raises urllib.error.URLError on network failure.
    """
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


def _extract_state_from_municipio(item: dict) -> str | None:
    """Extract state abbreviation from an IBGE município entry, trying both nested paths."""
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

    Returns a list of dicts with keys 'nome' and 'sigla' (state abbreviation).
    """
    print(f"  Fetching {IBGE_MUNICIPIOS_URL} …")
    data: list[dict] = _fetch_json(IBGE_MUNICIPIOS_URL)

    result, skipped = [], 0
    for item in data:
        sigla = _extract_state_from_municipio(item)
        if sigla is None:
            skipped += 1
            continue
        result.append({"nome": item["nome"], "sigla": sigla})

    if skipped:
        print(f"  Warning: {skipped} município entries skipped (could not resolve state)")
    print(f"  {len(result)} municipalities loaded")
    return result


def fetch_ibge_distritos() -> list[dict[str, str]]:
    """
    Fetch all Brazilian districts from the IBGE API.

    Returns a list of dicts with keys 'nome' and 'sigla' (state abbreviation of
    the parent municipality).
    """
    print(f"  Fetching {IBGE_DISTRITOS_URL} …")
    data: list[dict] = _fetch_json(IBGE_DISTRITOS_URL)

    result, skipped = [], 0
    for item in data:
        try:
            municipio = item["municipio"]
            sigla = _extract_state_from_municipio(municipio)
            if sigla is None:
                raise ValueError
            result.append({"nome": item["nome"], "sigla": sigla})
        except (TypeError, KeyError, ValueError):
            skipped += 1

    if skipped:
        print(f"  Warning: {skipped} distrito entries skipped (could not resolve state)")
    print(f"  {len(result)} districts loaded")
    return result


# ---------------------------------------------------------------------------
# CSV loading
# ---------------------------------------------------------------------------


def load_pair_counts() -> dict[tuple[str, str], dict[str, int]]:
    """
    Count raw row occurrences of each (staged_city, staged_state) pair per source.

    Returns a dict mapping (city, state) → {source_name: count}.
    """
    all_pair_counts: dict[tuple[str, str], dict[str, int]] = defaultdict(dict)

    for source_name, (csv_file, city_col, state_col) in SOURCES.items():
        print(f"  {csv_file} …")
        df = pd.read_csv(
            DATA_DIR / csv_file,
            usecols=[city_col, state_col],
            dtype=str,
        ).dropna(subset=[city_col, state_col])

        df["_city"] = df[city_col].map(stage_city)
        df["_state"] = df[state_col].map(stage_state)

        for (city, state), count in df.groupby(["_city", "_state"]).size().items():
            all_pair_counts[(city, state)][source_name] = int(count)

        print(f"    {df.groupby(['_city', '_state']).ngroups} distinct pairs  |  sample: {list(df.groupby(['_city', '_state']).groups.keys())[:3]}")

    return all_pair_counts


def load_zip_for_pairs() -> dict[tuple[str, str], Counter]:
    """
    For each (staged_city, staged_state) pair, collect all associated zip code prefixes
    from every row across all three source files.

    Zip prefixes are zero-padded to 5 digits (e.g. 1037 → '01037').
    Returns a dict mapping (city, state) → Counter of zip prefix strings.
    """
    pair_to_zips: dict[tuple[str, str], Counter] = defaultdict(Counter)

    for source_name, (csv_file, city_col, state_col) in SOURCES.items():
        zip_col = ZIP_COL[source_name]
        df = pd.read_csv(
            DATA_DIR / csv_file,
            usecols=[city_col, state_col, zip_col],
        ).dropna(subset=[city_col, state_col, zip_col])

        df["_city"] = df[city_col].astype(str).map(stage_city)
        df["_state"] = df[state_col].astype(str).map(stage_state)
        # Zero-pad the integer zip prefix to 5 digits
        df["_zip"] = df[zip_col].astype(int).apply(lambda z: str(z).zfill(5))

        for (city, state, zip_code), count in df.groupby(["_city", "_state", "_zip"]).size().items():
            pair_to_zips[(city, state)][zip_code] += int(count)

    return pair_to_zips


# ---------------------------------------------------------------------------
# ViaCEP lookup
# ---------------------------------------------------------------------------


def query_viacep(zip_prefix: str) -> dict | None:
    """
    Query the ViaCEP API for a 5-digit zip code prefix (padded with '000').

    Returns the response dict on success (containing at least 'localidade' and 'uf'),
    or None if the request fails, the CEP is not found, or the response is invalid.
    """
    cep = zip_prefix + "000"
    url = VIACEP_URL.format(cep=cep)
    try:
        data = _fetch_json(url, timeout=10)
        if isinstance(data, dict) and "erro" not in data and "localidade" in data:
            return data
        return None
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Fuzzy matching
# ---------------------------------------------------------------------------


def best_fuzzy_match(
    norm_city: str,
    norm_state: str,
    municipio_by_norm_state: dict[str, list[tuple[str, str]]],
) -> tuple[str | None, float]:
    """
    Find the highest-scoring município match for a normalised (city, state) pair.

    Candidates are restricted to the same normalised state. Similarity is computed
    with difflib.SequenceMatcher.

    Returns (original_ibge_nome, score) if score ≥ FUZZY_THRESHOLD, else (None, best_score).
    """
    candidates = municipio_by_norm_state.get(norm_state, [])
    if not candidates:
        return None, 0.0

    best_score = 0.0
    best_name: str | None = None
    for norm_candidate, orig_name in candidates:
        score = difflib.SequenceMatcher(None, norm_city, norm_candidate).ratio()
        if score > best_score:
            best_score = score
            best_name = orig_name

    if best_score >= FUZZY_THRESHOLD:
        return best_name, best_score
    return None, best_score


# ---------------------------------------------------------------------------
# Report helpers
# ---------------------------------------------------------------------------


def md_table(rows: list[list[str]], headers: list[str]) -> str:
    """Render a list of rows as a GitHub-Flavoured Markdown table."""
    sep = "|" + "|".join("---" for _ in headers) + "|"
    header_line = "| " + " | ".join(headers) + " |"
    body = "\n".join("| " + " | ".join(row) + " |" for row in rows)
    return "\n".join([header_line, sep, body])


def render_section_table(
    entries: list[dict],
    extra_headers: list[str],
    extra_col_fns: list,
) -> str:
    """
    Render a section table sorted by affected row count (descending).

    entries        — list of dicts with keys: city, state, sources, total_rows
    extra_headers  — additional column headers after "Affected rows"
    extra_col_fns  — callables (entry → str) for each extra column
    """
    base_headers = ["Raw city", "State", "Sources", "Affected rows"]
    sorted_entries = sorted(entries, key=lambda x: x["total_rows"], reverse=True)
    rows = []
    for e in sorted_entries:
        row = [
            f"`{e['city']}`",
            e["state"],
            ", ".join(e["sources"]),
            str(e["total_rows"]),
        ]
        row.extend(fn(e) for fn in extra_col_fns)
        rows.append(row)
    return md_table(rows, base_headers + extra_headers)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    """Run the four-tier validation pipeline and write the structured mismatch report."""

    # --- Fetch IBGE reference data ---
    print("Fetching IBGE reference data …")
    municipios = fetch_ibge_municipios()
    distritos = fetch_ibge_distritos()

    print("\nMunicípio sample (first 3):")
    for m in municipios[:3]:
        print(f"  nome={m['nome']!r}  sigla={m['sigla']!r}")
    print("\nDistrito sample (first 3):")
    for d in distritos[:3]:
        print(f"  nome={d['nome']!r}  sigla={d['sigla']!r}")

    # Build normalised lookup structures
    municipio_norm_set: set[tuple[str, str]] = set()
    municipio_by_norm_state: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for m in municipios:
        nc, ns = normalize(m["nome"]), normalize(m["sigla"])
        municipio_norm_set.add((nc, ns))
        municipio_by_norm_state[ns].append((nc, m["nome"]))

    distrito_norm_set: set[tuple[str, str]] = set()
    for d in distritos:
        nc, ns = normalize(d["nome"]), normalize(d["sigla"])
        distrito_norm_set.add((nc, ns))

    # --- Load source CSVs ---
    print("\nLoading source CSVs …")
    all_pair_counts = load_pair_counts()
    total_distinct = len(all_pair_counts)
    print(f"\nTotal distinct (city, state) pairs across all sources: {total_distinct}")

    print("\nLoading zip code associations …")
    pair_to_zips = load_zip_for_pairs()

    # --- Tiers 1–3: município / distrito / fuzzy ---
    print("\nTier 1 & 2: município and distrito classification …")

    municipio_count = 0
    distrito_matches: list[dict] = []
    fuzzy_suggestions: list[dict] = []   # Section 3
    pending_viacep: list[dict] = []      # Candidates for tier 4

    for (city, state), source_counts in all_pair_counts.items():
        nc, ns = normalize(city), normalize(state)
        total_rows = sum(source_counts.values())
        sources_list = sorted(source_counts.keys())

        # Tier 1: município exact match
        if (nc, ns) in municipio_norm_set:
            municipio_count += 1
            continue

        # Tier 2: distrito exact match
        if (nc, ns) in distrito_norm_set:
            distrito_matches.append({
                "city": city, "state": state,
                "sources": sources_list, "total_rows": total_rows,
            })
            continue

        # Tier 3: fuzzy match against município list
        suggestion, score = best_fuzzy_match(nc, ns, municipio_by_norm_state)
        entry = {
            "city": city, "state": state,
            "sources": sources_list, "total_rows": total_rows,
            "suggestion": suggestion, "score": score,
        }

        if suggestion is not None:
            fuzzy_suggestions.append(entry)   # Section 3: confident correction found
        else:
            pending_viacep.append(entry)       # No confident match yet → try ViaCEP

    print(f"  Município matches:  {municipio_count}")
    print(f"  Distrito matches:   {len(distrito_matches)}")
    print(f"  Fuzzy suggestions:  {len(fuzzy_suggestions)}")
    print(f"  Pending ViaCEP:     {len(pending_viacep)}")

    # --- Tier 4: ViaCEP lookup ---
    print(f"\nTier 4: querying ViaCEP for {len(pending_viacep)} unresolved pairs …")
    print(f"  (delay: {VIACEP_DELAY}s per request — estimated {len(pending_viacep) * VIACEP_DELAY:.0f}s)")

    viacep_matches: list[dict] = []    # Section 4
    no_confident_match: list[dict] = []  # Section 5

    for i, entry in enumerate(pending_viacep, start=1):
        city, state = entry["city"], entry["state"]

        zip_counter = pair_to_zips.get((city, state), Counter())
        if not zip_counter:
            no_confident_match.append(entry)
            continue

        zip_prefix = zip_counter.most_common(1)[0][0]
        result = query_viacep(zip_prefix)
        time.sleep(VIACEP_DELAY)

        if result:
            entry["viacep_localidade"] = result.get("localidade", "")
            entry["viacep_uf"] = result.get("uf", "")
            entry["cep_used"] = zip_prefix + "-000"
            viacep_matches.append(entry)
        else:
            no_confident_match.append(entry)

        if i % 25 == 0 or i == len(pending_viacep):
            print(f"  {i}/{len(pending_viacep)} queried …")

    print(f"\n  ViaCEP matches:     {len(viacep_matches)}")
    print(f"  No confident match: {len(no_confident_match)}")

    # --- Summary stats ---
    total_matched = municipio_count + len(distrito_matches)
    match_pct = 100 * total_matched / total_distinct if total_distinct else 0.0
    resolved_pct = 100 * (total_matched + len(viacep_matches)) / total_distinct if total_distinct else 0.0

    # --- Write report ---
    print("\nWriting report …")

    lines: list[str] = [
        "# City Name Mismatch Report",
        "",
        f"Generated: {date.today()}",
        "",
        "---",
        "",
        "## Summary",
        "",
        md_table(
            [
                ["IBGE municipalities", str(len(municipios))],
                ["IBGE districts", str(len(distritos))],
                ["Distinct (city, state) pairs in our data", str(total_distinct)],
                ["", ""],
                ["1. Matched at município level", str(municipio_count)],
                ["2. Matched at distrito level", str(len(distrito_matches))],
                ["3. Fuzzy suggestion available", str(len(fuzzy_suggestions))],
                ["4. Matched via ViaCEP", str(len(viacep_matches))],
                ["5. No confident match", str(len(no_confident_match))],
                ["", ""],
                ["IBGE exact match rate (tiers 1 + 2)", f"{match_pct:.1f}%"],
                ["Overall resolution rate (tiers 1 + 2 + 4)", f"{resolved_pct:.1f}%"],
            ],
            ["Metric", "Value"],
        ),
        "",
        f"Fuzzy threshold: {FUZZY_THRESHOLD} (SequenceMatcher ratio, same-state candidates only).",
        f"ViaCEP CEP format: 5-digit zip prefix + '000'.",
        "",
        "---",
        "",
        "## Section 1 — Matched at município level",
        "",
        f"{municipio_count} pairs matched exactly against the IBGE município list after normalisation.",
        "No action required for these.",
        "",
        "---",
        "",
        "## Section 2 — Matched at distrito level",
        "",
        f"{len(distrito_matches)} pairs matched the IBGE distrito list but not the município list.",
        "These are valid Brazilian administrative units at district granularity.",
        "",
    ]

    if distrito_matches:
        lines += [render_section_table(distrito_matches, [], []), ""]
    else:
        lines += ["_None found._", ""]

    lines += [
        "---",
        "",
        "## Section 3 — Fuzzy suggestion available",
        "",
        f"{len(fuzzy_suggestions)} pairs did not match at município or distrito level,",
        f"but fuzzy matching found a município candidate with similarity ≥ {FUZZY_THRESHOLD} in the same state.",
        "These are likely spelling variants, hyphenation differences, or typos of known municipalities.",
        "",
    ]

    if fuzzy_suggestions:
        lines += [
            render_section_table(
                fuzzy_suggestions,
                ["Suggested correction", "Similarity"],
                [
                    lambda e: e["suggestion"] or "—",
                    lambda e: f"{e['score']:.2f}",
                ],
            ),
            "",
        ]
    else:
        lines += ["_None found._", ""]

    lines += [
        "---",
        "",
        "## Section 4 — Matched via ViaCEP",
        "",
        f"{len(viacep_matches)} pairs were unresolved after tiers 1–3 but the most common associated",
        "zip code returned a valid result from ViaCEP. The official localidade and UF are recorded.",
        "",
    ]

    if viacep_matches:
        lines += [
            render_section_table(
                viacep_matches,
                ["ViaCEP localidade", "ViaCEP UF", "CEP used"],
                [
                    lambda e: e["viacep_localidade"],
                    lambda e: e["viacep_uf"],
                    lambda e: e["cep_used"],
                ],
            ),
            "",
        ]
    else:
        lines += ["_None found._", ""]

    lines += [
        "---",
        "",
        "## Section 5 — No confident match",
        "",
        f"{len(no_confident_match)} pairs remain unresolved after all four tiers.",
        "These may be subdistricts, neighbourhoods, historical names, corrupt data, or",
        "zip codes that return no result in ViaCEP.",
        "",
    ]

    if no_confident_match:
        lines += [
            render_section_table(
                no_confident_match,
                ["Best fuzzy candidate", "Score"],
                [
                    lambda e: e.get("suggestion") or "—",
                    lambda e: f"{e['score']:.2f}" if e.get("score", 0) > 0 else "—",
                ],
            ),
            "",
        ]
    else:
        lines += ["_None found._", ""]

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"Report written → {REPORT_PATH.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
