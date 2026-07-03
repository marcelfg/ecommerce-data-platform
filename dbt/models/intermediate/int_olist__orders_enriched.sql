WITH orders AS (

    SELECT * FROM {{ ref('stg_olist__orders') }}

),

customers_enriched AS (

    SELECT * FROM {{ ref('int_olist__customers_enriched') }}

),

payments_aggregated AS (

    SELECT * FROM {{ ref('int_olist__order_payments_aggregated') }}

),

reviews_aggregated AS (

    SELECT * FROM {{ ref('int_olist__order_reviews_aggregated') }}

),

enriched AS (

    SELECT
        o.order_id,
        o.customer_id,
        customers_enriched.customer_unique_id,
        customers_enriched.customer_city,
        customers_enriched.customer_state,
        customers_enriched.latitude                                                         AS customer_latitude,
        customers_enriched.longitude                                                        AS customer_longitude,
        o.order_status,
        o.order_purchased_at,
        o.order_approved_at,
        o.order_delivered_to_carrier_at,
        o.order_delivered_to_customer_at,
        o.order_estimated_delivery_at,
        DATEDIFF(DAY, o.order_purchased_at, o.order_approved_at)                            AS days_to_approval,
        DATEDIFF(DAY, o.order_approved_at, o.order_delivered_to_carrier_at)                 AS days_to_carrier,
        DATEDIFF(DAY, o.order_delivered_to_carrier_at, o.order_delivered_to_customer_at)    AS days_to_customer,
        DATEDIFF(DAY, o.order_purchased_at, o.order_delivered_to_customer_at)               AS delivery_lead_time,
        DATEDIFF(DAY, o.order_estimated_delivery_at, o.order_delivered_to_customer_at)      AS delivery_delay_days,
        o.order_delivered_to_customer_at > o.order_estimated_delivery_at                    AS is_late_delivery,
        TO_CHAR(o.order_purchased_at, 'YYYY-MM')                                            AS order_purchase_month,
        HOUR(o.order_purchased_at)                                                          AS purchase_hour,
        DAYNAME(o.order_purchased_at)                                                       AS purchase_day_of_week,
        payments_aggregated.total_payment_value,
        payments_aggregated.has_split_payment,
        payments_aggregated.primary_payment_type,
        reviews_aggregated.avg_review_score,
        reviews_aggregated.overall_sentiment,
        o._loaded_at
    FROM orders AS o
    LEFT JOIN customers_enriched
        ON o.customer_id = customers_enriched.customer_id
    LEFT JOIN payments_aggregated
        ON o.order_id = payments_aggregated.order_id
    LEFT JOIN reviews_aggregated
        ON o.order_id = reviews_aggregated.order_id
    QUALIFY ROW_NUMBER() OVER (
        PARTITION BY o.order_id
        ORDER BY o._loaded_at DESC
    ) = 1

)

SELECT * FROM enriched