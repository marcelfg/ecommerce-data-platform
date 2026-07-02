WITH customers AS (

    SELECT * FROM {{ ref('stg_olist__customers') }}

),

standardization AS (

    SELECT * FROM {{ ref('location_standardization') }}

),

geolocation AS (

    SELECT * FROM {{ ref('int_olist__geolocation_aggregated') }}

),

enriched AS (

    SELECT
        customers.customer_id,
        customers.customer_unique_id,
        customers.customer_zip_code,
        COALESCE(standardization.standardized_city, customers.customer_city) AS customer_city,
        COALESCE(standardization.standardized_state, customers.customer_state) AS customer_state,
        geolocation.latitude,
        geolocation.longitude,
        customers._loaded_at
    FROM customers
    LEFT JOIN standardization
        ON LOWER(TRIM(customers.customer_city)) = LOWER(TRIM(standardization.raw_city))
        AND LOWER(TRIM(customers.customer_state)) = LOWER(TRIM(standardization.raw_state))
    LEFT JOIN geolocation
        ON customers.customer_zip_code = geolocation.zip_code
    QUALIFY ROW_NUMBER() OVER (
        PARTITION BY customers.customer_id
        ORDER BY customers._loaded_at DESC
    ) = 1

)

SELECT * FROM enriched