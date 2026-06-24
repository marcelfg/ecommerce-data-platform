WITH geolocation AS (

    SELECT * FROM {{ ref('stg_olist__geolocation') }}

),

standardization AS (

    SELECT * FROM {{ ref('location_standardization') }}

),

cleaned AS (

    SELECT
        geolocation.zip_code,
        geolocation.latitude,
        geolocation.longitude,
        COALESCE(standardization.standardized_city, geolocation.city) AS city,
        COALESCE(standardization.standardized_state, geolocation.state) AS state
    FROM geolocation
    LEFT JOIN standardization
        ON LOWER(TRIM(geolocation.city)) = LOWER(TRIM(standardization.raw_city))
        AND LOWER(TRIM(geolocation.state)) = LOWER(TRIM(standardization.raw_state))

),

deduplicated AS (

    SELECT DISTINCT
        zip_code,
        city,
        state,
        latitude,
        longitude
    FROM cleaned

),

aggregated AS (

    SELECT
        zip_code,
        city,
        state,
        AVG(latitude) AS latitude,
        AVG(longitude) AS longitude
    FROM deduplicated
    GROUP BY zip_code, city, state
    -- To handle cases where a zip code is incorrectly associated with a city.
    QUALIFY ROW_NUMBER() OVER (
        PARTITION BY zip_code
        ORDER BY COUNT(*) DESC
    ) = 1

)

SELECT * FROM aggregated