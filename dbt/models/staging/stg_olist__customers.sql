WITH source AS (

    SELECT * FROM {{ source('raw', 'customers') }}

),

renamed AS (

    SELECT
        customer_id,
        customer_unique_id,
        customer_zip_code_prefix      AS customer_zip_code,
        LOWER(TRIM(customer_city))    AS customer_city,
        UPPER(TRIM(customer_state))   AS customer_state,
        _loaded_at::TIMESTAMP_NTZ     AS _loaded_at
    FROM source

)

SELECT * FROM renamed