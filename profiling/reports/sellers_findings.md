# Sellers Dataset — Profiling Findings

**Source file:** `data/olist_sellers_dataset.csv`
**Profiled on:** 2026-06-18
**Script:** `profiling/scripts/sellers_profile.py`

---

## 1. Shape and Dtypes

| Metric | Value |
|---|---|
| Rows | 3,095 |
| Columns | 4 |

| Column | Dtype |
|---|---|
| `seller_id` | str |
| `seller_zip_code_prefix` | str |
| `seller_city` | str |
| `seller_state` | str |

All columns are string. `seller_zip_code_prefix` is forced to `str` on load to preserve leading zeros.

---

## 2. Missing Values

No nulls in any column. `not_null` dbt tests are safe on all four columns.

---

## 3. Exact Duplicate Rows

Zero exact duplicates. The dataset is clean at the row level.

---

## 4. ID Uniqueness

`seller_id` is 100% unique across all 3,095 rows. The `unique` + `not_null` dbt tests are valid.

---

## 5. Zip Code Format

| Length | Count |
|---|---|
| 5 | 3,095 |

All zip codes are exactly 5 characters. 33.2% (1,027 rows) begin with a leading zero, confirming the VARCHAR decision is essential.

---

## 6. State Distribution

All values are valid Brazilian state codes. No unrecognised values. The `accepted_values` dbt test is safe.

Top states by seller count: SP (1,849 — 60%), PR (349 — 11%), MG (244 — 8%).

**Decision:** `UPPER(TRIM(seller_state))` applied in staging as a defensive transform.

---

## 7. City Name Quality

| Metric | Count |
|---|---|
| Total rows | 3,095 |
| Leading/trailing whitespace | 0 |
| Entirely lowercase | 3,066 (99.1%) |
| Entirely uppercase | 0 |
| Mixed / other | 29 (0.9%) |
| Unique city values | 611 |

99.1% of city names are entirely lowercase. The 29 mixed rows contain accented characters — valid city names, not data quality issues.

**Decision:** `LOWER(TRIM(seller_city))` applied in staging to normalise casing and guard against whitespace ingestion artifacts.
