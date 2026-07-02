WITH sellers AS (

    SELECT * FROM {{ ref('stg_olist__sellers') }}

),

standardization AS (

    SELECT * FROM {{ ref('location_standardization') }}

),

geolocation AS (

    SELECT * FROM {{ ref('int_olist__geolocation_aggregated') }}

),

enriched AS (

    SELECT
        sellers.seller_id,
        sellers.seller_zip_code,
        COALESCE(standardization.standardized_city, sellers.seller_city) AS seller_city,
        COALESCE(standardization.standardized_state, sellers.seller_state) AS seller_state,
        geolocation.latitude,
        geolocation.longitude,
        sellers._loaded_at
    FROM sellers
    LEFT JOIN standardization
        ON LOWER(TRIM(sellers.seller_city)) = LOWER(TRIM(standardization.raw_city))
        AND LOWER(TRIM(sellers.seller_state)) = LOWER(TRIM(standardization.raw_state))
    LEFT JOIN geolocation
        ON sellers.seller_zip_code = geolocation.zip_code
    QUALIFY ROW_NUMBER() OVER (
        PARTITION BY sellers.seller_id
        ORDER BY sellers._loaded_at DESC
    ) = 1

)

SELECT * FROM enriched
