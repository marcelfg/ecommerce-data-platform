WITH products AS (

    SELECT * FROM {{ ref('stg_olist__products') }}

),

deduped AS (

    SELECT *
    FROM products
    QUALIFY ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY _loaded_at DESC) = 1

)

SELECT * FROM deduped
