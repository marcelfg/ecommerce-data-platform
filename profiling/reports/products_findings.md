# Products Dataset — Profiling Findings

**Source file:** `data/olist_products_dataset.csv`
**Profiled on:** 2026-06-18
**Script:** `profiling/scripts/products_profile.py`

---

## 1. Shape and Dtypes

| Metric | Value |
|---|---|
| Rows | 32,951 |
| Columns | 9 |

| Column | Raw dtype | Notes |
|---|---|---|
| `product_id` | str | UUID identifier |
| `product_category_name` | str | Portuguese category name |
| `product_name_lenght` | float64 | Typo — should be `length`. Float due to NULLs |
| `product_description_lenght` | float64 | Typo — should be `length`. Float due to NULLs |
| `product_photos_qty` | float64 | Float due to NULLs |
| `product_weight_g` | float64 | Float due to NULLs |
| `product_length_cm` | float64 | Float due to NULLs |
| `product_height_cm` | float64 | Float due to NULLs |
| `product_width_cm` | float64 | Float due to NULLs |

All seven numeric columns load as `float64` because pandas promotes integer columns to float when NULLs are present. The underlying values are integers and should be cast accordingly in Snowflake.

**Decision:** Two column name typos (`product_name_lenght`, `product_description_lenght`) are corrected to `name_length` and `description_length` in the staging model. All numeric columns cast to `INT` via `TRY_CAST`.

---

## 2. Missing Values

| Column | Null count | Null % |
|---|---|---|
| `product_id` | 0 | 0.00% |
| `product_category_name` | 610 | 1.85% |
| `product_name_lenght` | 610 | 1.85% |
| `product_description_lenght` | 610 | 1.85% |
| `product_photos_qty` | 610 | 1.85% |
| `product_weight_g` | 2 | 0.01% |
| `product_length_cm` | 2 | 0.01% |
| `product_height_cm` | 2 | 0.01% |
| `product_width_cm` | 2 | 0.01% |

Two distinct null patterns:

- **610 products (1.85%)** have nulls simultaneously across `category_name`, `name_length`, `description_length`, and `photos_qty`. These products have a valid `product_id` and physical dimensions but no catalogue metadata — likely products that were listed but never fully catalogued.
- **2 products (0.01%)** have nulls across all four physical dimension columns (`weight_g`, `length_cm`, `height_cm`, `width_cm`). These have valid IDs and catalogue metadata but no shipping dimensions.

**Decision:** `not_null` tests are omitted for all columns except `product_id` and `_loaded_at`. NULLs are preserved at staging and handled downstream.

---

## 3. Exact Duplicate Rows

Zero exact duplicates. The dataset is clean at the row level.

---

## 4. ID Uniqueness

`product_id` is 100% unique across all 32,951 rows. The `unique` + `not_null` dbt tests are valid.

---

## 5. Category Name Distribution

| Metric | Value |
|---|---|
| Unique categories | 73 |
| Null values | 610 |

Category names are Portuguese with underscores (e.g. `cama_mesa_banho`, `esporte_lazer`). A separate source table (`product_category_name_translation`) maps these to English — translation belongs in an intermediate or mart model, not staging.

Top 5 categories: `cama_mesa_banho` (3,029), `esporte_lazer` (2,867), `moveis_decoracao` (2,657), `beleza_saude` (2,444), `utilidades_domesticas` (2,335).

---

## 6. Numeric Columns — Ranges and Zero Values

| Column | Min | Max | Mean | Nulls | Zeros |
|---|---|---|---|---|---|
| `product_name_lenght` | 5 | 76 | 48.5 | 610 | 0 |
| `product_description_lenght` | 4 | 3,992 | 771.5 | 610 | 0 |
| `product_photos_qty` | 1 | 20 | 2.2 | 610 | 0 |
| `product_weight_g` | 0 | 40,425 | 2,276.5 | 2 | 4 |
| `product_length_cm` | 7 | 105 | 30.8 | 2 | 0 |
| `product_height_cm` | 2 | 105 | 16.9 | 2 | 0 |
| `product_width_cm` | 6 | 118 | 23.2 | 2 | 0 |

- **4 products have `weight_g = 0`** — physically implausible. These are likely data entry errors. Preserved at staging; downstream models should filter or flag zero-weight products before calculating freight costs.
- `product_description_lenght` has a wide range (4–3,992 characters) — no action needed at staging.
- All dimension columns (`length_cm`, `height_cm`, `width_cm`) have sensible ranges with no zero values.
- `product_photos_qty` minimum of 1 (for non-null rows) — no products have zero photos when the field is populated.
