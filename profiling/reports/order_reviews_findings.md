# Order Reviews Dataset — Profiling Findings

**Source file:** `data/olist_order_reviews_dataset.csv`
**Profiled on:** 2026-06-18
**Script:** `profiling/scripts/order_reviews_profile.py`

---

## 1. Shape and Dtypes

| Metric | Value |
|---|---|
| Rows | 99,224 |
| Columns | 7 |

| Column | Dtype |
|---|---|
| `review_id` | str |
| `order_id` | str |
| `review_score` | int64 |
| `review_comment_title` | str |
| `review_comment_message` | str |
| `review_creation_date` | datetime64[us] |
| `review_answer_timestamp` | datetime64[us] |

`review_score` parses as int64. Both timestamp columns parse cleanly. `review_creation_date` contains full datetimes despite the `_date` suffix — the staging model renames it to `created_at`.

---

## 2. Missing Values

| Column | Null count | Null % |
|---|---|---|
| `review_id` | 0 | 0.00% |
| `order_id` | 0 | 0.00% |
| `review_score` | 0 | 0.00% |
| `review_comment_title` | 87,656 | 88.34% |
| `review_comment_message` | 58,247 | 58.70% |
| `review_creation_date` | 0 | 0.00% |
| `review_answer_timestamp` | 0 | 0.00% |

Comment fields are sparsely populated — only 11.7% of reviews include a title and 41.3% include a message. Both are expected nullable fields. `not_null` tests are not applied to either.

---

## 3. Exact Duplicate Rows

Zero exact duplicates. The dataset is clean at the row level.

---

## 4. ID Uniqueness

| ID Column | Total | Unique | Duplicates |
|---|---|---|---|
| `review_id` | 99,224 | 98,410 | 814 |
| `order_id` | 99,224 | 98,673 | 551 |

**`review_id` is not unique** — 814 rows share a `review_id` with at least one other row. This is a source data quality issue. No `unique` test should be applied to `review_id` at staging. Deduplication belongs in a downstream model once the business rule for resolving duplicate review IDs is established.

`order_id` duplicates indicate some orders received more than one review, which is also a source characteristic rather than an error.

---

## 5. Review Score Distribution

| Score | Count |
|---|---|
| 1 | 11,424 |
| 2 | 3,151 |
| 3 | 8,179 |
| 4 | 19,142 |
| 5 | 57,328 |

All scores are within the valid 1–5 range. Score 5 accounts for 57.8% of reviews. The `accepted_values` dbt test is safe.

---

## 6. Comment Field Population

| Field | Populated | % |
|---|---|---|
| `review_comment_title` | 11,568 | 11.7% |
| `review_comment_message` | 40,977 | 41.3% |

Both fields are optional. No transformations applied beyond renaming.

---

## 7. Timestamp Ranges

| Column | Nulls | Min | Max |
|---|---|---|---|
| `review_creation_date` | 0 | 2016-10-02 | 2018-08-31 |
| `review_answer_timestamp` | 0 | 2016-10-07 | 2018-10-29 |

No nulls. Ranges are plausible. `review_creation_date` has time-of-day zeroed out (00:00:00) for all rows — it is a date truncated to midnight rather than a true timestamp, but is kept as TIMESTAMP_NTZ for schema consistency.
