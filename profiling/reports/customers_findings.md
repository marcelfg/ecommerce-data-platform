# Customers Dataset — Profiling Findings

**Source file:** `data/olist_customers_dataset.csv`
**Profiled on:** 2026-06-18
**Script:** `profiling/scripts/customers_profile.py`

---

## 1. Shape and Dtypes

| Metric | Value |
|---|---|
| Rows | 99,441 |
| Columns | 5 |

| Column | Dtype |
|---|---|
| `customer_id` | str |
| `customer_unique_id` | str |
| `customer_zip_code_prefix` | str |
| `customer_city` | str |
| `customer_state` | str |

All columns are string — appropriate for ID and categorical fields. No numeric casting needed. `customer_zip_code_prefix` is forced to `str` on load to preserve leading zeros.

---

## 2. Missing Values

No nulls in any column. `not_null` dbt tests are safe on all five columns.

---

## 3. Exact Duplicate Rows

Zero exact duplicates. The dataset is clean at the row level.

---

## 4. ID Uniqueness

| ID Column | Total | Unique | Duplicates |
|---|---|---|---|
| `customer_id` | 99,441 | 99,441 | 0 |
| `customer_unique_id` | 99,441 | 96,096 | 3,345 |

- **`customer_id` is 100% unique** — it is the order-level customer identifier. The `unique` + `not_null` dbt tests are valid.
- **`customer_unique_id` has 3,345 repeated values** — this is expected and by design. It is the cross-order identifier tying multiple orders to the same physical customer. The top customer placed 17 orders. No `unique` test should be applied to this column.

---

## 5. Zip Code Format

| Length | Count |
|---|---|
| 5 | 99,441 |

All 99,441 zip codes are exactly 5 characters — no truncation or padding issues. 24.1% (23,995 rows) begin with a leading zero. Casting to integer would silently corrupt these values, so `zip_code` must remain VARCHAR.

---

## 6. State Distribution

All 27 Brazilian state/territory codes are present. No unrecognised values. The `accepted_values` dbt test is safe.

Top states by customer count: SP (41,746 — 42%), RJ (12,852 — 13%), MG (11,635 — 12%).

**Decision:** `UPPER(TRIM(customer_state))` applied in staging — all values are already uppercase with no whitespace, but the defensive transform makes the model resilient to future ingestion variation.

---

## 7. City Name Quality

| Metric | Count |
|---|---|
| Total rows | 99,441 |
| Leading/trailing whitespace | 0 |
| Entirely lowercase | 99,214 (99.8%) |
| Entirely uppercase | 0 |
| Mixed / other | 227 (0.2%) |
| Unique city values | 4,119 |

99.8% of city names are entirely lowercase. The 227 mixed rows contain accented characters (e.g. `são paulo`, `goiânia`) — valid city names that fall outside the ASCII lowercase range, not data quality issues.

**Decision:** `LOWER(TRIM(customer_city))` applied in staging. The data is nearly clean, but the transform normalises casing and guards against whitespace ingestion artifacts consistently.
