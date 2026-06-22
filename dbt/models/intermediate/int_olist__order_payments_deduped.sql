WITH order_payments AS (

    SELECT * FROM {{ ref('stg_olist__order_payments') }}

),

deduped AS (

    SELECT *
    FROM order_payments
    QUALIFY ROW_NUMBER() OVER (PARTITION BY order_id, payment_sequential ORDER BY _loaded_at DESC) = 1

)

SELECT * FROM deduped
