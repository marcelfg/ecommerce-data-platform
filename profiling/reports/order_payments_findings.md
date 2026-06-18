# Order Payments Dataset — Profiling Findings

**Source file:** `data/olist_order_payments_dataset.csv`
**Profiled on:** 2026-06-18
**Script:** `profiling/scripts/order_payments_profile.py`

---

## 1. Shape and Dtypes

| Metric | Value |
|---|---|
| Rows | 103,886 |
| Columns | 5 |

| Column | Dtype |
|---|---|
| `order_id` | str |
| `payment_sequential` | int64 |
| `payment_type` | str |
| `payment_installments` | int64 |
| `payment_value` | float64 |

`payment_sequential` and `payment_installments` parse as int64 with no nulls. `payment_value` is float64.

---

## 2. Missing Values

No nulls in any column. `not_null` dbt tests are safe on all columns.

---

## 3. Exact Duplicate Rows

Zero exact duplicates. The dataset is clean at the row level.

---

## 4. Composite Primary Key

The unique identifier is the combination of `order_id` + `payment_sequential`. All 103,886 combinations are unique — the composite `unique_combination_of` test is safe.

---

## 5. Payment Type Distribution

| Type | Count |
|---|---|
| credit_card | 76,795 |
| boleto | 19,784 |
| voucher | 5,775 |
| debit_card | 1,529 |
| not_defined | 3 |

All 5 values are recognised. The `accepted_values` dbt test is safe. `not_defined` is a valid catch-all for unclassified payment methods.

---

## 6. Payment Installments

| Metric | Value |
|---|---|
| Min | 0 |
| Max | 24 |
| Mean | 2.85 |
| Nulls | 0 |
| Zeros | 2 |

2 rows have `payment_installments = 0`. These correspond to payment types that don't use installments (e.g. vouchers or `not_defined`). Preserved at staging; downstream models should account for this when calculating instalment-based metrics.

---

## 7. Payment Value

| Metric | Value |
|---|---|
| Min | 0.00 |
| Max | 13,664.08 |
| Mean | 154.10 |
| Nulls | 0 |
| Zeros | 9 |
| Negatives | 0 |

9 rows have `payment_value = 0.00`. These are likely fully-voucher-covered orders with no monetary transaction. Preserved at staging.
