WITH customers AS (

    SELECT * FROM {{ ref('int_olist__customers_deduped') }}

),

standardization AS (

    SELECT * FROM {{ ref('location_standardization') }}

),

cleaned AS (

    SELECT
        customers.customer_id,
        customers.customer_unique_id,
        customers.customer_zip_code,
        COALESCE(standardization.standardized_city, customers.customer_city) AS customer_city,
        COALESCE(standardization.standardized_state, customers.customer_state) AS customer_state,
        customers._loaded_at
    FROM customers
    LEFT JOIN standardization
        ON LOWER(TRIM(customers.customer_city)) = LOWER(TRIM(standardization.raw_city))
        AND LOWER(TRIM(customers.customer_state)) = LOWER(TRIM(standardization.raw_state))

)

SELECT * FROM cleaned
