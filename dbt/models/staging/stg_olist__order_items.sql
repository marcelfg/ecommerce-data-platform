WITH source AS (

    SELECT * FROM {{ source('raw', 'order_items') }}

),

renamed AS (

    SELECT
        order_id,
        order_item_id,
        product_id,
        seller_id,
        TRY_TO_TIMESTAMP_NTZ(shipping_limit_date)   AS shipping_limit_at,
        TRY_CAST(price AS NUMBER(10,2))             AS price,
        TRY_CAST(freight_value AS NUMBER(10,2))     AS freight_value,
        _loaded_at::TIMESTAMP_NTZ                   AS _loaded_at
    FROM source

)

SELECT * FROM renamed
