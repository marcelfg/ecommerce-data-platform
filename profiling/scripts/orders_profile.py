"""
orders_profile.py

Profiles data/olist_orders_dataset.csv to understand data quality
before building the stg_olist__orders dbt model.

Checks performed:
- Shape and column dtypes
- Missing values per column
- Exact duplicate rows
- order_id uniqueness
- order_status distribution
- Timestamp nulls and date ranges
- Date ordering sanity check (purchase → approved → carrier → customer)

Usage:
    uv run python profiling/scripts/orders_profile.py
"""

from pathlib import Path

import pandas as pd

VALID_STATUSES = {
    "delivered", "shipped", "canceled", "unavailable",
    "invoiced", "processing", "created", "approved",
}

DATA_PATH = Path(__file__).parent.parent.parent / "data" / "olist_orders_dataset.csv"

TIMESTAMP_COLS = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
]


def load_data(path: Path) -> pd.DataFrame:
    """Load the orders CSV into a DataFrame, parsing timestamps."""
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
    """Check uniqueness of order_id."""
    print("=" * 60)
    print("ID UNIQUENESS")
    print("=" * 60)
    total = len(df)
    unique = df["order_id"].nunique()
    dupes = total - unique
    print(f"order_id — total: {total:,}  unique: {unique:,}  duplicates: {dupes:,}")
    print()


def profile_order_status(df: pd.DataFrame) -> None:
    """Print status distribution and flag any unrecognised values."""
    print("=" * 60)
    print("ORDER STATUS DISTRIBUTION")
    print("=" * 60)
    status_counts = df["order_status"].value_counts()
    print(status_counts.to_string())
    print()
    unknown = df[~df["order_status"].isin(VALID_STATUSES)]
    print(f"Rows with unrecognised status values: {len(unknown):,}")
    if not unknown.empty:
        print(unknown["order_status"].value_counts().to_string())
    print()


def profile_timestamps(df: pd.DataFrame) -> None:
    """Print null counts and date ranges for all timestamp columns."""
    print("=" * 60)
    print("TIMESTAMP NULLS AND RANGES")
    print("=" * 60)
    for col in TIMESTAMP_COLS:
        s = df[col]
        nulls = s.isnull().sum()
        if s.notna().any():
            print(f"{col}")
            print(f"  nulls={nulls:,}  min={s.min()}  max={s.max()}")
        else:
            print(f"{col}  — all null")
    print()


def profile_date_ordering(df: pd.DataFrame) -> None:
    """Check that timestamps follow the expected chronological order."""
    print("=" * 60)
    print("DATE ORDERING SANITY CHECKS")
    print("=" * 60)
    checks = [
        ("purchase before approved",
         df["order_purchase_timestamp"] > df["order_approved_at"]),
        ("approved before carrier delivery",
         df["order_approved_at"] > df["order_delivered_carrier_date"]),
        ("carrier delivery before customer delivery",
         df["order_delivered_carrier_date"] > df["order_delivered_customer_date"]),
    ]
    for label, mask in checks:
        violations = mask.sum()
        print(f"  {label}: {violations:,} violations")
    print()


def main() -> None:
    """Run all profiling checks and print results."""
    df = load_data(DATA_PATH)
    profile_shape_and_dtypes(df)
    profile_missing_values(df)
    profile_exact_duplicates(df)
    profile_id_uniqueness(df)
    profile_order_status(df)
    profile_timestamps(df)
    profile_date_ordering(df)
    print("Profiling complete.")


if __name__ == "__main__":
    main()
