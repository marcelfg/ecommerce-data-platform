WITH orders AS (

    SELECT * FROM {{ ref('int_olist__orders_enriched') }}

),

preferred_payment AS (

    SELECT
        customer_unique_id,
        primary_payment_type
    FROM orders
    GROUP BY customer_unique_id, primary_payment_type
    QUALIFY ROW_NUMBER() OVER (
        PARTITION BY customer_unique_id
        ORDER BY COUNT(*) DESC
    ) = 1

),

aggregated AS (

    SELECT
        orders.customer_unique_id,
        CAST(MIN(orders.order_purchased_at) AS DATE)                            AS first_purchase_date,
        CAST(MAX(orders.order_purchased_at) AS DATE)                            AS latest_purchase_date,
        DATEDIFF(
            DAY,
            MIN(orders.order_purchased_at),
            MAX(orders.order_purchased_at)
        )                                                                       AS customer_lifespan_days,
        SUM(orders.total_payment_value)                                         AS lifetime_revenue,
        COUNT(DISTINCT orders.order_id)                                         AS lifetime_order_count,
        SUM(orders.total_payment_value) / COUNT(DISTINCT orders.order_id)       AS average_order_value,
        COUNT(DISTINCT orders.order_id) > 1                                     AS is_repeat_customer,
        AVG(orders.avg_review_score)                                            AS avg_review_score_given,
        preferred_payment.primary_payment_type                                  AS preferred_payment_type
    FROM orders
    LEFT JOIN preferred_payment
        ON orders.customer_unique_id = preferred_payment.customer_unique_id
    GROUP BY
        orders.customer_unique_id,
        preferred_payment.primary_payment_type

)

SELECT * FROM aggregated