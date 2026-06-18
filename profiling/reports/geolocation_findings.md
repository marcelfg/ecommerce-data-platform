# Geolocation Dataset — Profiling Findings

**Source file:** `data/olist_geolocation_dataset.csv`
**Profiled on:** 2026-06-18
**Script:** `profiling/scripts/geolocation_profile.py`

---

## 1. Shape and Dtypes

| Metric | Value |
|---|---|
| Rows | 1,000,163 |
| Columns | 5 |

| Column | Dtype |
|---|---|
| `geolocation_zip_code_prefix` | str |
| `geolocation_lat` | float64 |
| `geolocation_lng` | float64 |
| `geolocation_city` | str |
| `geolocation_state` | str |

**Decision:** Lat/lng arrive as `float64` — pandas can parse them cleanly. `TRY_CAST(... AS NUMBER(8,6))` / `NUMBER(9,6)` will apply the correct precision in Snowflake without risk of a cast failure on the current data.

---

## 2. Missing Values

No nulls in any column. `not_null` dbt tests are safe on all five columns.

---

## 3. Exact Duplicate Rows

**261,831 rows are fully identical (26.18% of total).**

These are complete duplicates — same zip code, same lat/lng, same city, same state. They inflate the dataset by more than a quarter and offer no additional geographic information.

**Decision:** Keep all rows at staging (staging should mirror the raw layer). Flag for deduplication in an intermediate model before joining to other tables. A `WHERE` filter or `QUALIFY ROW_NUMBER() OVER (PARTITION BY zip_code, lat, lng, city, state ORDER BY 1) = 1` in intermediate will address this.

---

## 4. Zip Code Duplicates

| Metric | Value |
|---|---|
| Unique zip codes | 19,015 |
| Zip codes with more than 1 row | 17,972 (94.5%) |
| Median rows per zip code | 29 |
| Max rows for one zip code | 1,146 (`24220`) |

This is a source design characteristic: each zip code maps to a geographic area, not a single point, so multiple lat/lng pairs are recorded per prefix. This is expected and not a defect.

**Decision:** No deduplication at staging. Downstream models that need a single representative point per zip should use an intermediate model.

---

## 5. Coordinate Range Analysis

| Metric | Latitude | Longitude |
|---|---|---|
| Min | −36.61 | −101.47 |
| Max | 45.07 | 121.11 |
| Mean | −21.18 | −46.39 |

**42 rows fall outside Brazil's bounding box** (lat −33.75 to 5.27, lng −73.99 to −34.79). Sample:

| zip_code | lat | lng | state |
|---|---|---|---|
| 28165 | 41.61 | −8.41 | RJ | ← Portugal |
| 28155 | −34.59 | −58.73 | RJ | ← Argentina |
| 28155 | 42.44 | 13.82 | RJ | ← Italy |
| 29654 | 29.41 | −98.48 | ES | ← Texas, USA |
| 29654 | 21.66 | −101.47 | ES | ← Mexico |

These are geocoding errors — real Brazilian zip codes assigned coordinates on other continents.

**Decision:** `TRY_CAST` does not filter these (they are valid numbers). Keep them at staging to preserve the raw state. Flag for filtering in intermediate/marts using a bounding box predicate. Document in column descriptions so downstream developers are aware.

---

## 6. State Distribution

All 27 Brazilian state/territory codes are present. No unrecognised values. The `accepted_values` dbt test is safe.

Top states by row count: SP (404,268), MG (126,336), RJ (121,169), RS (61,851), PR (57,859).

---

## 7. City Name Quality

| Metric | Count |
|---|---|
| Total rows | 1,000,163 |
| Leading/trailing whitespace | 0 |
| Entirely lowercase | 925,382 (92.5%) |
| Mixed / other | 74,781 (7.5%) |
| Unique city values | 8,011 |

The "mixed/other" 7.5% includes several issues observed in the sample:

| Value | Issue |
|---|---|
| `são paulo` | Accented characters — not caught by the lowercase regex, but valid |
| `jundiaí` | Same — accented, valid |
| `sãopaulo` | Missing space — geocoding artifact |
| `sa£o paulo` | Encoding corruption (`£` instead of `ã`) |
| `sp` | State abbreviation used as city name |

**Decision:** `LOWER(TRIM(city))` normalises casing and removes any whitespace padding. It does not repair encoding corruption or missing spaces — those require more complex normalisation that belongs in an intermediate model. At staging, we standardise what we can and preserve the rest faithfully.
