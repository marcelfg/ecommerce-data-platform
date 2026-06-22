WITH product_category_name_translation AS (

    SELECT * FROM {{ ref('stg_olist__product_category_name_translation') }}

),

deduped AS (

    SELECT *
    FROM product_category_name_translation
    QUALIFY ROW_NUMBER() OVER (PARTITION BY product_category_name_pt ORDER BY _loaded_at DESC) = 1

)

SELECT * FROM deduped
