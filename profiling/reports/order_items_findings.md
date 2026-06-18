# Order Items Dataset — Profiling Findings

**Source file:** `data/olist_order_items_dataset.csv`
**Profiled on:** 2026-06-18
**Script:** `profiling/scripts/order_items_profile.py`

---

## 1. Shape and Dtypes

| Metric | Value |
|---|---|
| Rows | 112,650 |
| Columns | 7 |

| Column | Dtype |
|---|---|
| `order_id` | str |
| `order_item_id` | int64 |
| `product_id` | str |
| `seller_id` | str |
| `shipping_limit_date` | datetime64[us] |
| `price` | float64 |
| `freight_value` | float64 |

`order_item_id` parses as int64 with no nulls. `shipping_limit_date` parses cleanly as datetime — the `_date` suffix is a misnomer as it contains full datetimes; the staging model renames it to `shipping_limit_at`.

---

## 2. Missing Values

No nulls in any column. `not_null` dbt tests are safe on all columns.

---

## 3. Exact Duplicate Rows

Zero exact duplicates. The dataset is clean at the row level.

---

## 4. Composite Primary Key

This table has no single-column primary key. The unique identifier is the combination of `order_id` + `order_item_id`. All 112,650 combinations are unique — the composite `unique_combination_of` test is safe.

---

## 5. Order Item ID Distribution

| Metric | Value |
|---|---|
| Max order_item_id | 21 |
| Mean items per order | 1.14 |

`order_item_id` is a sequential integer starting at 1 within each order. Most orders contain a single item (87.6%). The maximum of 21 items in a single order is plausible for bulk purchases.

---

## 6. Monetary Columns

| Column | Min | Max | Mean | Nulls | Zeros | Negatives |
|---|---|---|---|---|---|---|
| `price` | 0.85 | 6,735.00 | 120.65 | 0 | 0 | 0 |
| `freight_value` | 0.00 | 409.68 | 19.99 | 0 | 383 | 0 |

- `price` is clean — no zeros, no negatives, no nulls.
- `freight_value` has 383 zero values, consistent with free shipping promotions. No negatives or nulls.

Both columns cast to `NUMBER(10,2)` in the staging model.

---

## 7. Shipping Limit Date

No nulls. Range spans 2016-09-19 to 2020-04-09. The upper bound extends slightly beyond the order dataset range, which is expected — shipping deadlines are set in advance of fulfilment.
