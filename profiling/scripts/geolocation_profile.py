"""
geolocation_profile.py

Profiles data/olist_geolocation_dataset.csv to understand data quality
before building the stg_olist__geolocation dbt model.

Checks performed:
- Shape and column dtypes
- Missing values per column
- Exact duplicate rows
- Duplicate zip code prefixes (expected — multiple coordinate points per zip)
- Coordinate range validity (Brazil bounding box)
- State value distribution and unknown state codes
- City name quality (whitespace, mixed case)
- Top zip codes by row count

Usage:
    uv run python profiling/scripts/geolocation_profile.py
"""

from pathlib import Path

import pandas as pd

BRAZIL_LAT_MIN = -33.75
BRAZIL_LAT_MAX = 5.27
BRAZIL_LNG_MIN = -73.99
BRAZIL_LNG_MAX = -34.79

VALID_STATES = {
    "AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO",
    "MA", "MG", "MS", "MT", "PA", "PB", "PE", "PI", "PR",
    "RJ", "RN", "RO", "RR", "RS", "SC", "SE", "SP", "TO",
}

DATA_PATH = Path(__file__).parent.parent.parent / "data" / "olist_geolocation_dataset.csv"


def load_data(path: Path) -> pd.DataFrame:
    """Load the geolocation CSV into a DataFrame."""
    print(f"Loading data from {path} ...")
    df = pd.read_csv(path, dtype={"geolocation_zip_code_prefix": str})
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


def profile_zip_code_duplicates(df: pd.DataFrame) -> None:
    """Show how many zip codes appear more than once (expected in this dataset)."""
    print("=" * 60)
    print("ZIP CODE DUPLICATE ANALYSIS")
    print("=" * 60)
    zip_counts = df["geolocation_zip_code_prefix"].value_counts()
    total_zips = zip_counts.shape[0]
    multi_row_zips = (zip_counts > 1).sum()
    print(f"Unique zip codes          : {total_zips:,}")
    print(f"Zip codes with >1 row     : {multi_row_zips:,} ({multi_row_zips / total_zips * 100:.1f}%)")
    print(f"Max rows for one zip code : {zip_counts.max()}")
    print(f"Median rows per zip code  : {zip_counts.median():.1f}")
    print()
    print("Top 10 zip codes by row count:")
    print(zip_counts.head(10).to_string())
    print()


def profile_coordinate_ranges(df: pd.DataFrame) -> None:
    """Check lat/lng distributions and flag values outside Brazil's bounding box."""
    print("=" * 60)
    print("COORDINATE RANGE ANALYSIS")
    print("=" * 60)
    lat = df["geolocation_lat"]
    lng = df["geolocation_lng"]

    print("Latitude  — min: {:.6f}  max: {:.6f}  mean: {:.6f}".format(
        lat.min(), lat.max(), lat.mean()))
    print("Longitude — min: {:.6f}  max: {:.6f}  mean: {:.6f}".format(
        lng.min(), lng.max(), lng.mean()))
    print()

    out_of_bounds = df[
        (lat < BRAZIL_LAT_MIN) | (lat > BRAZIL_LAT_MAX) |
        (lng < BRAZIL_LNG_MIN) | (lng > BRAZIL_LNG_MAX)
    ]
    print(f"Rows outside Brazil bounding box: {len(out_of_bounds):,}")
    if not out_of_bounds.empty:
        print(out_of_bounds[["geolocation_zip_code_prefix",
                              "geolocation_lat",
                              "geolocation_lng",
                              "geolocation_state"]].head(10).to_string(index=False))
    print()


def profile_states(df: pd.DataFrame) -> None:
    """Print state distribution and flag any unrecognised state codes."""
    print("=" * 60)
    print("STATE DISTRIBUTION")
    print("=" * 60)
    state_counts = df["geolocation_state"].value_counts().sort_index()
    print(state_counts.to_string())
    print()

    unknown = df[~df["geolocation_state"].isin(VALID_STATES)]
    print(f"Rows with unrecognised state codes: {len(unknown):,}")
    if not unknown.empty:
        print(unknown["geolocation_state"].value_counts().to_string())
    print()


def profile_city_quality(df: pd.DataFrame) -> None:
    """Check city name casing consistency and leading/trailing whitespace."""
    print("=" * 60)
    print("CITY NAME QUALITY")
    print("=" * 60)
    cities = df["geolocation_city"]
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
    profile_zip_code_duplicates(df)
    profile_coordinate_ranges(df)
    profile_states(df)
    profile_city_quality(df)
    print("Profiling complete.")


if __name__ == "__main__":
    main()
