WITH order_items AS (

    SELECT * FROM {{ ref('stg_olist__order_items') }}

),

products_enriched AS (

    SELECT * FROM {{ ref('int_olist__products_enriched') }}

),

sellers_enriched AS (

    SELECT * FROM {{ ref('int_olist__sellers_enriched') }}

),

enriched AS (

    SELECT
        oi.order_id,
        oi.order_item_id,
        oi.product_id,
        p.product_category,
        p.weight_g                                                                          AS product_weight_g,
        p.length_cm                                                                         AS product_length_cm,
        p.height_cm                                                                         AS product_height_cm,
        p.width_cm                                                                          AS product_width_cm,
        p.length_cm * p.height_cm * p.width_cm                                              AS product_volume_cm3,
        oi.seller_id,
        s.seller_city,
        s.seller_state,
        s.latitude                                                                          AS seller_latitude,
        s.longitude                                                                         AS seller_longitude,
        oi.shipping_limit_at,
        oi.price,
        oi.freight_value,
        oi.price + oi.freight_value                                                         AS total_item_value,
        oi.freight_value / NULLIF(oi.price, 0)                                              AS freight_ratio,
        oi._loaded_at
    FROM order_items AS oi
    LEFT JOIN products_enriched AS p
        ON oi.product_id = p.product_id
    LEFT JOIN sellers_enriched AS s
        ON oi.seller_id = s.seller_id
    QUALIFY ROW_NUMBER() OVER (
        PARTITION BY oi.order_id, oi.order_item_id
        ORDER BY oi._loaded_at DESC
    ) = 1

)

SELECT * FROM enriched