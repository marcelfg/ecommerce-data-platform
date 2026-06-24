WITH sellers AS (

    SELECT * FROM {{ ref('int_olist__sellers_deduped') }}

),

standardization AS (

    SELECT * FROM {{ ref('location_standardization') }}

),

cleaned AS (

    SELECT
        sellers.seller_id,
        sellers.seller_zip_code,
        COALESCE(standardization.standardized_city, sellers.seller_city) AS seller_city,
        COALESCE(standardization.standardized_state, sellers.seller_state) AS seller_state,
        sellers._loaded_at
    FROM sellers
    LEFT JOIN standardization
        ON LOWER(TRIM(sellers.seller_city)) = LOWER(TRIM(standardization.raw_city))
        AND LOWER(TRIM(sellers.seller_state)) = LOWER(TRIM(standardization.raw_state))

)

SELECT * FROM cleaned
