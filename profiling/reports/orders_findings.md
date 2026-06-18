# Orders Dataset — Profiling Findings

**Source file:** `data/olist_orders_dataset.csv`
**Profiled on:** 2026-06-18
**Script:** `profiling/scripts/orders_profile.py`

---

## 1. Shape and Dtypes

| Metric | Value |
|---|---|
| Rows | 99,441 |
| Columns | 8 |

| Column | Dtype |
|---|---|
| `order_id` | str |
| `customer_id` | str |
| `order_status` | str |
| `order_purchase_timestamp` | datetime64[us] |
| `order_approved_at` | datetime64[us] |
| `order_delivered_carrier_date` | datetime64[us] |
| `order_delivered_customer_date` | datetime64[us] |
| `order_estimated_delivery_date` | datetime64[us] |

All five timestamp columns parse cleanly to datetime. The `_date` suffix on three columns is a misnomer — they contain full datetimes, not dates. The staging model renames them with an `_at` suffix for consistency.

---

## 2. Missing Values

| Column | Null count | Null % |
|---|---|---|
| `order_id` | 0 | 0.00% |
| `customer_id` | 0 | 0.00% |
| `order_status` | 0 | 0.00% |
| `order_purchase_timestamp` | 0 | 0.00% |
| `order_approved_at` | 160 | 0.16% |
| `order_delivered_carrier_date` | 1,783 | 1.79% |
| `order_delivered_customer_date` | 2,965 | 2.98% |
| `order_estimated_delivery_date` | 0 | 0.00% |

Nulls follow the expected lifecycle pattern — an order can exist without having been approved, handed to a carrier, or delivered. All are preserved at staging. `not_null` tests are applied only to `order_id`, `customer_id`, `order_status`, `order_purchase_timestamp`, `order_estimated_delivery_date`, and `_loaded_at`.

---

## 3. Exact Duplicate Rows

Zero exact duplicates. The dataset is clean at the row level.

---

## 4. ID Uniqueness

`order_id` is 100% unique across all 99,441 rows. The `unique` + `not_null` dbt tests are valid.

---

## 5. Order Status Distribution

| Status | Count |
|---|---|
| delivered | 96,478 |
| shipped | 1,107 |
| canceled | 625 |
| unavailable | 609 |
| invoiced | 314 |
| processing | 301 |
| created | 5 |
| approved | 2 |

All 8 status values are recognised. The `accepted_values` dbt test is safe.

---

## 6. Timestamp Ranges

| Column | Nulls | Min | Max |
|---|---|---|---|
| `order_purchase_timestamp` | 0 | 2016-09-04 | 2018-10-17 |
| `order_approved_at` | 160 | 2016-09-15 | 2018-09-03 |
| `order_delivered_carrier_date` | 1,783 | 2016-10-08 | 2018-09-11 |
| `order_delivered_customer_date` | 2,965 | 2016-10-11 | 2018-10-17 |
| `order_estimated_delivery_date` | 0 | 2016-09-30 | 2018-11-12 |

Data spans September 2016 to October 2018. All ranges are plausible.

---

## 7. Date Ordering Sanity Checks

| Check | Violations |
|---|---|
| purchase before approved | 0 |
| approved before carrier delivery | 1,359 |
| carrier delivery before customer delivery | 23 |

The 1,359 cases where `approved_at` is later than `delivered_carrier_date` are likely system logging delays rather than true chronological errors — the approval event may have been recorded after the carrier already scanned the parcel. The 23 carrier/customer inversion cases are similar. All records are preserved at staging; downstream models should account for these when calculating fulfilment durations.
