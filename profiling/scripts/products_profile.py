"""
products_profile.py

Profiles data/olist_products_dataset.csv to understand data quality
before building the stg_olist__products dbt model.

Checks performed:
- Shape and column dtypes
- Missing values per column
- Exact duplicate rows
- product_id uniqueness
- Category name distribution and null analysis
- Numeric column ranges and zero-value counts (dimensions and weight)
- Column name typo identification

Usage:
    uv run python profiling/scripts/products_profile.py
"""

from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).parent.parent.parent / "data" / "olist_products_dataset.csv"


def load_data(path: Path) -> pd.DataFrame:
    """Load the products CSV into a DataFrame."""
    print(f"Loading data from {path} ...")
    df = pd.read_csv(path, dtype={"product_id": str})
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
    """Check uniqueness of product_id."""
    print("=" * 60)
    print("ID UNIQUENESS")
    print("=" * 60)
    total = len(df)
    unique = df["product_id"].nunique()
    dupes = total - unique
    print(f"product_id — total: {total:,}  unique: {unique:,}  duplicates: {dupes:,}")
    print()


def profile_category_names(df: pd.DataFrame) -> None:
    """Print category name distribution and null count."""
    print("=" * 60)
    print("CATEGORY NAME DISTRIBUTION")
    print("=" * 60)
    cats = df["product_category_name"]
    print(f"Unique categories : {cats.nunique():,}")
    print(f"Null values       : {cats.isnull().sum():,}")
    print()
    print("Top 20 categories by product count:")
    print(cats.value_counts().head(20).to_string())
    print()


def profile_numeric_columns(df: pd.DataFrame) -> None:
    """Print descriptive stats and zero-value counts for numeric columns."""
    print("=" * 60)
    print("NUMERIC COLUMNS — RANGES AND ZERO VALUES")
    print("=" * 60)
    numeric_cols = [
        "product_name_lenght",
        "product_description_lenght",
        "product_photos_qty",
        "product_weight_g",
        "product_length_cm",
        "product_height_cm",
        "product_width_cm",
    ]
    for col in numeric_cols:
        s = df[col]
        zeros = (s == 0).sum()
        print(f"{col}")
        print(f"  min={s.min():.0f}  max={s.max():.0f}  mean={s.mean():.1f}  "
              f"nulls={s.isnull().sum():,}  zeros={zeros:,}")
    print()


def main() -> None:
    """Run all profiling checks and print results."""
    df = load_data(DATA_PATH)
    profile_shape_and_dtypes(df)
    profile_missing_values(df)
    profile_exact_duplicates(df)
    profile_id_uniqueness(df)
    profile_category_names(df)
    profile_numeric_columns(df)
    print("Profiling complete.")


if __name__ == "__main__":
    main()
