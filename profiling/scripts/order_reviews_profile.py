"""
order_reviews_profile.py

Profiles data/olist_order_reviews_dataset.csv to understand data quality
before building the stg_olist__order_reviews dbt model.

Checks performed:
- Shape and column dtypes
- Missing values per column
- Exact duplicate rows
- review_id uniqueness
- review_score distribution
- Comment field population (title and message)
- Timestamp ranges

Usage:
    uv run python profiling/scripts/order_reviews_profile.py
"""

from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).parent.parent.parent / "data" / "olist_order_reviews_dataset.csv"

TIMESTAMP_COLS = ["review_creation_date", "review_answer_timestamp"]


def load_data(path: Path) -> pd.DataFrame:
    """Load the order reviews CSV into a DataFrame."""
    print(f"Loading data from {path} ...")
    df = pd.read_csv(path, parse_dates=TIMESTAMP_COLS)
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
    """Check uniqueness of review_id and whether order_id repeats."""
    print("=" * 60)
    print("ID UNIQUENESS")
    print("=" * 60)
    total = len(df)
    rid_unique = df["review_id"].nunique()
    oid_unique = df["order_id"].nunique()
    print(f"review_id — total: {total:,}  unique: {rid_unique:,}  duplicates: {total - rid_unique:,}")
    print(f"order_id  — total: {total:,}  unique: {oid_unique:,}  duplicates: {total - oid_unique:,}")
    print()


def profile_review_score(df: pd.DataFrame) -> None:
    """Print score distribution and flag out-of-range values."""
    print("=" * 60)
    print("REVIEW SCORE DISTRIBUTION")
    print("=" * 60)
    score_counts = df["review_score"].value_counts().sort_index()
    print(score_counts.to_string())
    print()
    out_of_range = df[(df["review_score"] < 1) | (df["review_score"] > 5)]
    print(f"Scores outside 1–5 range: {len(out_of_range):,}")
    print()


def profile_comment_fields(df: pd.DataFrame) -> None:
    """Check population rate of comment title and message fields."""
    print("=" * 60)
    print("COMMENT FIELD POPULATION")
    print("=" * 60)
    total = len(df)
    for col in ["review_comment_title", "review_comment_message"]:
        populated = df[col].notna().sum()
        pct = populated / total * 100
        print(f"{col}: {populated:,} populated ({pct:.1f}%)")
    print()


def profile_timestamps(df: pd.DataFrame) -> None:
    """Print null counts and date ranges for timestamp columns."""
    print("=" * 60)
    print("TIMESTAMP RANGES")
    print("=" * 60)
    for col in TIMESTAMP_COLS:
        s = df[col]
        print(f"{col}")
        print(f"  nulls={s.isnull().sum():,}  min={s.min()}  max={s.max()}")
    print()


def main() -> None:
    """Run all profiling checks and print results."""
    df = load_data(DATA_PATH)
    profile_shape_and_dtypes(df)
    profile_missing_values(df)
    profile_exact_duplicates(df)
    profile_id_uniqueness(df)
    profile_review_score(df)
    profile_comment_fields(df)
    profile_timestamps(df)
    print("Profiling complete.")


if __name__ == "__main__":
    main()
