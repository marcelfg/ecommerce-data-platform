"""
order_items_profile.py

Profiles data/olist_order_items_dataset.csv to understand data quality
before building the stg_olist__order_items dbt model.

Checks performed:
- Shape and column dtypes
- Missing values per column
- Exact duplicate rows
- Composite primary key uniqueness (order_id + order_item_id)
- order_item_id distribution (items per order)
- Monetary column ranges and zero/negative value counts
- Shipping limit date range and null check

Usage:
    uv run python profiling/scripts/order_items_profile.py
"""

from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).parent.parent.parent / "data" / "olist_order_items_dataset.csv"


def load_data(path: Path) -> pd.DataFrame:
    """Load the order items CSV into a DataFrame."""
    print(f"Loading data from {path} ...")
    df = pd.read_csv(path, parse_dates=["shipping_limit_date"])
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


def profile_primary_key(df: pd.DataFrame) -> None:
    """Check uniqueness of the composite primary key (order_id + order_item_id)."""
    print("=" * 60)
    print("COMPOSITE PRIMARY KEY (order_id + order_item_id)")
    print("=" * 60)
    total = len(df)
    unique = df[["order_id", "order_item_id"]].drop_duplicates().shape[0]
    dupes = total - unique
    print(f"Total rows          : {total:,}")
    print(f"Unique combinations : {unique:,}")
    print(f"Duplicates          : {dupes:,}")
    print()


def profile_item_id_distribution(df: pd.DataFrame) -> None:
    """Show distribution of order_item_id to understand items-per-order."""
    print("=" * 60)
    print("ORDER ITEM ID DISTRIBUTION")
    print("=" * 60)
    item_counts = df["order_item_id"].value_counts().sort_index()
    print(f"Max order_item_id : {df['order_item_id'].max()}")
    print(f"Mean items/order  : {df.groupby('order_id')['order_item_id'].max().mean():.2f}")
    print()
    print("order_item_id frequency (how many orders have N items):")
    print(item_counts.to_string())
    print()


def profile_monetary_columns(df: pd.DataFrame) -> None:
    """Print ranges and zero/negative counts for price and freight_value."""
    print("=" * 60)
    print("MONETARY COLUMNS — RANGES")
    print("=" * 60)
    for col in ["price", "freight_value"]:
        s = df[col]
        zeros = (s == 0).sum()
        negatives = (s < 0).sum()
        print(f"{col}")
        print(f"  min={s.min():.2f}  max={s.max():.2f}  mean={s.mean():.2f}  "
              f"nulls={s.isnull().sum():,}  zeros={zeros:,}  negatives={negatives:,}")
    print()


def profile_shipping_date(df: pd.DataFrame) -> None:
    """Print null count and range for the shipping limit date."""
    print("=" * 60)
    print("SHIPPING LIMIT DATE")
    print("=" * 60)
    s = df["shipping_limit_date"]
    print(f"nulls={s.isnull().sum():,}  min={s.min()}  max={s.max()}")
    print()


def main() -> None:
    """Run all profiling checks and print results."""
    df = load_data(DATA_PATH)
    profile_shape_and_dtypes(df)
    profile_missing_values(df)
    profile_exact_duplicates(df)
    profile_primary_key(df)
    profile_item_id_distribution(df)
    profile_monetary_columns(df)
    profile_shipping_date(df)
    print("Profiling complete.")


if __name__ == "__main__":
    main()
