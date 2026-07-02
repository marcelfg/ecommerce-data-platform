WITH order_reviews AS (

    SELECT * FROM {{ ref('stg_olist__order_reviews') }}

),

enriched AS (

    SELECT
        review_id,
        order_id,
        review_score,
        review_title,
        review_message,
        review_created_at,
        review_answered_at,
        DATEDIFF(
            DAY,
            review_created_at,
            review_answered_at
        )                                                               AS days_to_answer,
        review_message IS NOT NULL AND TRIM(review_message) != ''       AS has_message,
        CASE
            WHEN review_score IN (4, 5) THEN 'positive'
            WHEN review_score = 3       THEN 'neutral'
            WHEN review_score IN (1, 2) THEN 'negative'
        END                                                             AS review_sentiment,
        _loaded_at
    FROM order_reviews
    QUALIFY ROW_NUMBER() OVER (
        PARTITION BY order_id, review_id
        ORDER BY _loaded_at DESC
    ) = 1

)

SELECT * FROM enriched