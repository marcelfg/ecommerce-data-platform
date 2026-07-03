WITH order_payments AS (

    SELECT * FROM {{ ref('stg_olist__order_payments') }}

),

primary_payment AS (

    SELECT
        order_id,
        payment_type                                                                                                        AS primary_payment_type
    FROM order_payments
    QUALIFY ROW_NUMBER() OVER (
        PARTITION BY order_id
        ORDER BY payment_value DESC
    ) = 1

),

aggregated AS (

    SELECT
        op.order_id,
        SUM(op.payment_value)                                                                                               AS total_payment_value,
        COUNT(DISTINCT op.payment_type) > 1                                                                                 AS has_split_payment,
        COUNT(DISTINCT op.payment_type)                                                                                     AS number_of_payment_types,
        LISTAGG(DISTINCT op.payment_type, ' | ') WITHIN GROUP (ORDER BY op.payment_type)                                    AS payment_types,
        pp.primary_payment_type,                                                                                             
        COUNT(CASE WHEN op.payment_type = 'voucher' THEN 1 END) > 0                                                         AS used_voucher,
        SUM(CASE WHEN op.payment_type = 'voucher' THEN op.payment_value END)                                                AS voucher_value,
        COUNT(CASE WHEN op.payment_type = 'credit_card' THEN 1 END) > 0                                                     AS used_credit_card,
        SUM(CASE WHEN op.payment_type = 'credit_card' THEN op.payment_value END)                                            AS credit_card_value
    FROM order_payments AS op
    LEFT JOIN primary_payment AS pp
        ON op.order_id = pp.order_id
    GROUP BY
        op.order_id,
        pp.primary_payment_type

)

SELECT * FROM aggregated