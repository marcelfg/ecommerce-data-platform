WITH products AS (

    SELECT * FROM {{ ref('int_olist__products_enriched') }}

),

final AS (

    SELECT
        product_id,
        product_category,
        product_name_length,
        product_description_length,
        product_photos_qty                                                    AS listing_photo_count,
        weight_g,
        length_cm,
        height_cm,
        width_cm,
        length_cm * height_cm * width_cm                                      AS product_volume_cm3
    FROM products

)

SELECT * FROM final