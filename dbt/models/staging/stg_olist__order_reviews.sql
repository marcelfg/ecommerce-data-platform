WITH source AS (

    SELECT * FROM {{ source('raw', 'order_reviews') }}

),

renamed AS (

    SELECT
        review_id,
        order_id,
        TRY_CAST(review_score AS INT)                 AS review_score,
        review_comment_title                          AS review_title,
        review_comment_message                        AS review_message,
        TRY_TO_TIMESTAMP_NTZ(review_creation_date)    AS review_created_at,
        TRY_TO_TIMESTAMP_NTZ(review_answer_timestamp) AS review_answered_at,
        _loaded_at::TIMESTAMP_NTZ                     AS _loaded_at
    FROM source

)

SELECT * FROM renamed
