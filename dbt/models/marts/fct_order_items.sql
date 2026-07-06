WITH order_items AS (

    SELECT * FROM {{ ref('int_olist__order_items_enriched') }}

),

orders AS (

    SELECT * FROM {{ ref('int_olist__orders_enriched') }}

),

final AS (

    SELECT
        order_items.order_id,
        order_items.order_item_id,
        order_items.product_id,
        order_items.seller_id,
        orders.order_purchased_at,
        order_items.shipping_limit_at,
        order_items.price,
        order_items.freight_value,
        order_items.total_item_value,
        order_items.freight_ratio
    FROM order_items
    LEFT JOIN orders
        ON order_items.order_id = orders.order_id

)

SELECT * FROM final