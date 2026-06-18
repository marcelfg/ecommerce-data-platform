WITH source AS (

    SELECT * FROM {{ source('raw', 'sellers') }}

),

renamed AS (

    SELECT
        seller_id,
        seller_zip_code_prefix    AS seller_zip_code,
        LOWER(TRIM(seller_city))  AS seller_city,
        UPPER(TRIM(seller_state)) AS seller_state,
        _loaded_at::TIMESTAMP_NTZ AS _loaded_at
    FROM source

)

SELECT * FROM renamed
