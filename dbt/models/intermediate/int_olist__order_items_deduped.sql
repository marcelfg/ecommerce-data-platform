WITH order_items AS (

    SELECT * FROM {{ ref('stg_olist__order_items') }}

),

deduped AS (

    SELECT *
    FROM order_items
    QUALIFY ROW_NUMBER() OVER (PARTITION BY order_id, order_item_id ORDER BY _loaded_at DESC) = 1

)

SELECT * FROM deduped
