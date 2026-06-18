"""
customers_profile.py

Profiles data/olist_customers_dataset.csv to understand data quality
and validate the existing stg_olist__customers dbt model.

Checks performed:
- Shape and column dtypes
- Missing values per column
- Exact duplicate rows
- customer_id uniqueness (expected: unique — order-level identifier)
- customer_unique_id cardinality (expected: fewer unique values — ties orders to a person)
- Zip code format (leading zeros, length)
- State value distribution and unknown state codes
- City name quality (whitespace, mixed case)

Usage:
    uv run python profiling/scripts/customers_profile.py
"""

from pathlib import Path

import pandas as pd

VALID_STATES = {
    "AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO",
    "MA", "MG", "MS", "MT", "PA", "PB", "PE", "PI", "PR",
    "RJ", "RN", "RO", "RR", "RS", "SC", "SE", "SP", "TO",
}

DATA_PATH = Path(__file__).parent.parent.parent / "data" / "olist_customers_dataset.csv"


def load_data(path: Path) -> pd.DataFrame:
    """Load the customers CSV into a DataFrame."""
    print(f"Loading data from {path} ...")
    df = pd.read_csv(path, dtype={"customer_zip_code_prefix": str})
    print(f"Loaded {len(df):,} rows x {len(df.columns)} columns.\n")
    return df


def profile_shape_and_dtypes(df: pd.DataFrame) -> None:
    """Print row/column counts and inferred column dtypes."""
    print("=" * 60)
    print("SHAPE AND DTYPES")
    print("=" * 60)
    print(f"Rows   : {len(df):,}")
    print(f"Columns: {len(df.columns)}")
    print()
    print(df.dtypes.to_string())
    print()


def profile_missing_values(df: pd.DataFrame) -> None:
    """Print count and percentage of nulls per column."""
    print("=" * 60)
    print("MISSING VALUES")
    print("=" * 60)
    missing = df.isnull().sum()
    pct = (missing / len(df) * 100).round(2)
    report = pd.DataFrame({"null_count": missing, "null_pct": pct})
    print(report.to_string())
    print()


def profile_exact_duplicates(df: pd.DataFrame) -> None:
    """Print count of fully duplicate rows (identical across all columns)."""
    print("=" * 60)
    print("EXACT DUPLICATE ROWS")
    print("=" * 60)
    n_dupes = df.duplicated().sum()
    print(f"Exact duplicate rows: {n_dupes:,} ({n_dupes / len(df) * 100:.2f}%)")
    print()


def profile_id_uniqueness(df: pd.DataFrame) -> None:
    """Check uniqueness of customer_id and cardinality of customer_unique_id."""
    print("=" * 60)
    print("ID UNIQUENESS")
    print("=" * 60)
    total = len(df)

    cid_unique = df["customer_id"].nunique()
    cid_dupes = total - cid_unique
    print(f"customer_id        — total: {total:,}  unique: {cid_unique:,}  duplicates: {cid_dupes:,}")

    uid_unique = df["customer_unique_id"].nunique()
    uid_dupes = total - uid_unique
    print(f"customer_unique_id — total: {total:,}  unique: {uid_unique:,}  duplicates: {uid_dupes:,}")
    print()

    if uid_dupes > 0:
        top_repeat = df["customer_unique_id"].value_counts().head(5)
        print("Top 5 customer_unique_id by order count (customers with most orders):")
        print(top_repeat.to_string())
    print()


def profile_zip_codes(df: pd.DataFrame) -> None:
    """Check zip code format — length and leading zeros."""
    print("=" * 60)
    print("ZIP CODE FORMAT")
    print("=" * 60)
    zips = df["customer_zip_code_prefix"]
    lengths = zips.str.len().value_counts().sort_index()
    print("Zip code length distribution:")
    print(lengths.to_string())
    print()
    leading_zero = zips.str.startswith("0").sum()
    print(f"Zip codes with leading zero: {leading_zero:,} ({leading_zero / len(zips) * 100:.1f}%)")
    print()


def profile_states(df: pd.DataFrame) -> None:
    """Print state distribution and flag any unrecognised state codes."""
    print("=" * 60)
    print("STATE DISTRIBUTION")
    print("=" * 60)
    state_counts = df["customer_state"].value_counts().sort_index()
    print(state_counts.to_string())
    print()

    unknown = df[~df["customer_state"].isin(VALID_STATES)]
    print(f"Rows with unrecognised state codes: {len(unknown):,}")
    if not unknown.empty:
        print(unknown["customer_state"].value_counts().to_string())
    print()


def profile_city_quality(df: pd.DataFrame) -> None:
    """Check city name casing consistency and leading/trailing whitespace."""
    print("=" * 60)
    print("CITY NAME QUALITY")
    print("=" * 60)
    cities = df["customer_city"]
    total = len(cities)

    has_leading_trailing_ws = cities.str.match(r"^\s|\s$").sum()
    is_uppercase = cities.str.match(r"^[A-Z\s]+$").sum()
    is_lowercase = cities.str.match(r"^[a-z\s\-]+$").sum()
    is_mixed = total - is_uppercase - is_lowercase

    print(f"Total rows                    : {total:,}")
    print(f"Rows with leading/trailing WS : {has_leading_trailing_ws:,}")
    print(f"Rows entirely lowercase       : {is_lowercase:,}")
    print(f"Rows entirely uppercase       : {is_uppercase:,}")
    print(f"Rows mixed / other            : {is_mixed:,}")
    print(f"Unique city values            : {cities.nunique():,}")
    print()
    print("Sample city values:")
    print(cities.drop_duplicates().head(10).to_string(index=False))
    print()


def main() -> None:
    """Run all profiling checks and print results."""
    df = load_data(DATA_PATH)
    profile_shape_and_dtypes(df)
    profile_missing_values(df)
    profile_exact_duplicates(df)
    profile_id_uniqueness(df)
    profile_zip_codes(df)
    profile_states(df)
    profile_city_quality(df)
    print("Profiling complete.")


if __name__ == "__main__":
    main()
