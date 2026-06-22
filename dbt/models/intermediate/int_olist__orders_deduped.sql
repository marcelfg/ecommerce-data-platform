WITH orders AS (

    SELECT * FROM {{ ref('stg_olist__orders') }}

),

deduped AS (

    SELECT *
    FROM orders
    QUALIFY ROW_NUMBER() OVER (PARTITION BY order_id ORDER BY _loaded_at DESC) = 1

)

SELECT * FROM deduped
