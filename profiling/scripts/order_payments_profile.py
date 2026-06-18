"""
order_payments_profile.py

Profiles data/olist_order_payments_dataset.csv to understand data quality
before building the stg_olist__order_payments dbt model.

Checks performed:
- Shape and column dtypes
- Missing values per column
- Exact duplicate rows
- Composite primary key uniqueness (order_id + payment_sequential)
- payment_type distribution and unknown values
- payment_installments range and zero-value count
- payment_value range, zero and negative counts

Usage:
    uv run python profiling/scripts/order_payments_profile.py
"""

from pathlib import Path

import pandas as pd

VALID_PAYMENT_TYPES = {"credit_card", "boleto", "voucher", "debit_card", "not_defined"}

DATA_PATH = Path(__file__).parent.parent.parent / "data" / "olist_order_payments_dataset.csv"


def load_data(path: Path) -> pd.DataFrame:
    """Load the order payments CSV into a DataFrame."""
    print(f"Loading data from {path} ...")
    df = pd.read_csv(path)
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
    """Check uniqueness of the composite primary key (order_id + payment_sequential)."""
    print("=" * 60)
    print("COMPOSITE PRIMARY KEY (order_id + payment_sequential)")
    print("=" * 60)
    total = len(df)
    unique = df[["order_id", "payment_sequential"]].drop_duplicates().shape[0]
    dupes = total - unique
    print(f"Total rows          : {total:,}")
    print(f"Unique combinations : {unique:,}")
    print(f"Duplicates          : {dupes:,}")
    print()


def profile_payment_type(df: pd.DataFrame) -> None:
    """Print payment type distribution and flag unknown values."""
    print("=" * 60)
    print("PAYMENT TYPE DISTRIBUTION")
    print("=" * 60)
    type_counts = df["payment_type"].value_counts()
    print(type_counts.to_string())
    print()
    unknown = df[~df["payment_type"].isin(VALID_PAYMENT_TYPES)]
    print(f"Rows with unrecognised payment types: {len(unknown):,}")
    if not unknown.empty:
        print(unknown["payment_type"].value_counts().to_string())
    print()


def profile_installments(df: pd.DataFrame) -> None:
    """Print range and zero-value count for payment_installments."""
    print("=" * 60)
    print("PAYMENT INSTALLMENTS")
    print("=" * 60)
    s = df["payment_installments"]
    zeros = (s == 0).sum()
    print(f"min={s.min()}  max={s.max()}  mean={s.mean():.2f}  "
          f"nulls={s.isnull().sum():,}  zeros={zeros:,}")
    print()
    print("Installment frequency:")
    print(s.value_counts().sort_index().to_string())
    print()


def profile_payment_value(df: pd.DataFrame) -> None:
    """Print range, zero and negative counts for payment_value."""
    print("=" * 60)
    print("PAYMENT VALUE")
    print("=" * 60)
    s = df["payment_value"]
    zeros = (s == 0).sum()
    negatives = (s < 0).sum()
    print(f"min={s.min():.2f}  max={s.max():.2f}  mean={s.mean():.2f}  "
          f"nulls={s.isnull().sum():,}  zeros={zeros:,}  negatives={negatives:,}")
    print()


def main() -> None:
    """Run all profiling checks and print results."""
    df = load_data(DATA_PATH)
    profile_shape_and_dtypes(df)
    profile_missing_values(df)
    profile_exact_duplicates(df)
    profile_primary_key(df)
    profile_payment_type(df)
    profile_installments(df)
    profile_payment_value(df)
    print("Profiling complete.")


if __name__ == "__main__":
    main()
