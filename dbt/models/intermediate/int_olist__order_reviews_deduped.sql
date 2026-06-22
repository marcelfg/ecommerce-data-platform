WITH order_reviews AS (

    SELECT * FROM {{ ref('stg_olist__order_reviews') }}

),

deduped AS (

    SELECT *
    FROM order_reviews
    QUALIFY ROW_NUMBER() OVER (PARTITION BY review_id, order_id ORDER BY _loaded_at DESC) = 1

)

SELECT * FROM deduped
