WITH source AS (

    SELECT * FROM {{ source('raw', 'orders') }}

),

renamed AS (

    SELECT
        order_id,
        customer_id,
        order_status,                                         
        TRY_TO_TIMESTAMP_NTZ(order_purchase_timestamp)       AS order_purchased_at,
        TRY_TO_TIMESTAMP_NTZ(order_approved_at)              AS order_approved_at,
        TRY_TO_TIMESTAMP_NTZ(order_delivered_carrier_date)   AS order_delivered_to_carrier_at,
        TRY_TO_TIMESTAMP_NTZ(order_delivered_customer_date)  AS order_delivered_to_customer_at,
        TRY_TO_TIMESTAMP_NTZ(order_estimated_delivery_date)  AS order_estimated_delivery_at,
        _loaded_at::TIMESTAMP_NTZ                            AS _loaded_at
    FROM source

)

SELECT * FROM renamed
