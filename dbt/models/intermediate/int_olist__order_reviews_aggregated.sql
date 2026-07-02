WITH order_reviews AS (

    SELECT * FROM {{ ref('int_olist__order_reviews_enriched') }}

),

aggregated AS (

    SELECT
        order_id,
        COUNT(review_id)                                                AS review_count,
        COUNT(review_id) > 1                                            AS has_multiple_reviews,
        COUNT(CASE WHEN has_message THEN 1 END)                         AS reviews_with_message,
        MIN(review_score)                                               AS min_review_score,
        MAX(review_score)                                               AS max_review_score,
        AVG(review_score)                                               AS avg_review_score,
        AVG(days_to_answer)                                             AS avg_days_to_answer,
        MIN(review_answered_at)                                         AS first_review_date,
        CASE
            WHEN AVG(review_score) >= 4 THEN 'positive'
            WHEN AVG(review_score) >= 3 THEN 'neutral'
            ELSE                             'negative'
        END                                                             AS overall_sentiment
    FROM order_reviews
    GROUP BY order_id

)

SELECT * FROM aggregated