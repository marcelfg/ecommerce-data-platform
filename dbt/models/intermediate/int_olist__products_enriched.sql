WITH products AS (

    SELECT * FROM {{ ref('stg_olist__products') }}

),

translations AS (

    SELECT * FROM {{ ref('stg_olist__product_category_name_translation') }}

),

enriched AS (

    SELECT
        products.product_id,
        translations.product_category_name_en AS product_category,
        products.product_name_length,
        products.product_description_length,
        products.product_photos_qty,
        products.weight_g,
        products.length_cm,
        products.height_cm,
        products.width_cm,
        products._loaded_at
    FROM products
    LEFT JOIN translations
        ON products.product_category_name = translations.product_category_name_pt
    QUALIFY ROW_NUMBER() OVER (
        PARTITION BY products.product_id
        ORDER BY products._loaded_at DESC
    ) = 1

)

SELECT * FROM enriched