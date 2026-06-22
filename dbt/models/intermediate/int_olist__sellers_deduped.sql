WITH sellers AS (

    SELECT * FROM {{ ref('stg_olist__sellers') }}

),

deduped AS (

    SELECT *
    FROM sellers
    QUALIFY ROW_NUMBER() OVER (PARTITION BY seller_id ORDER BY _loaded_at DESC) = 1

)

SELECT * FROM deduped
