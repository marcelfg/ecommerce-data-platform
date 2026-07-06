WITH orders_enriched AS (

    SELECT * FROM {{ ref('int_olist__orders_enriched') }}

),

order_items AS (

    SELECT * FROM {{ ref('int_olist__order_items_enriched') }}

),

payments_aggregated AS (

    SELECT * FROM {{ ref('int_olist__order_payments_aggregated') }}

),

items_aggregated AS (

    SELECT
        order_id,
        COUNT(*)                                                                    AS item_count,
        SUM(price)                                                                  AS total_price,
        SUM(freight_value)                                                          AS total_freight_value
    FROM order_items
    GROUP BY order_id

),

final AS (

    SELECT
        orders_enriched.order_id,
        orders_enriched.customer_unique_id,
        orders_enriched.customer_city                                                      AS shipping_city,
        orders_enriched.customer_state                                                     AS shipping_state,
        orders_enriched.customer_latitude                                                  AS shipping_latitude,
        orders_enriched.customer_longitude                                                 AS shipping_longitude,
        orders_enriched.order_status,
        orders_enriched.order_purchased_at,
        orders_enriched.delivery_lead_time,
        orders_enriched.delivery_delay_days,
        orders_enriched.is_late_delivery,
        items_aggregated.item_count,
        items_aggregated.total_price,                              
        items_aggregated.total_freight_value,
        orders_enriched.total_payment_value,
        orders_enriched.has_split_payment,
        orders_enriched.primary_payment_type,
        payments_aggregated.voucher_value / NULLIF(orders_enriched.total_payment_value, 0) AS discount_rate,
        orders_enriched.avg_review_score,
        orders_enriched.overall_sentiment
    FROM orders_enriched
    LEFT JOIN items_aggregated
        ON orders_enriched.order_id = items_aggregated.order_id
    LEFT JOIN payments_aggregated
        ON orders_enriched.order_id = payments_aggregated.order_id

)

SELECT * FROM final