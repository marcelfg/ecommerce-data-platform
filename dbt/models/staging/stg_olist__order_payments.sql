WITH source AS (

    SELECT * FROM {{ source('raw', 'order_payments') }}

),

renamed AS (

    SELECT
        order_id,
        TRY_CAST(payment_sequential AS INT)     AS payment_sequential,
        payment_type,
        TRY_CAST(payment_installments AS INT)   AS payment_installments,
        TRY_CAST(payment_value AS NUMBER(10,2)) AS payment_value,
        _loaded_at::TIMESTAMP_NTZ               AS _loaded_at
    FROM source

)

SELECT * FROM renamed
