WITH source AS (

    SELECT * FROM {{ source('raw', 'products') }}

),

renamed AS (

    SELECT
        product_id,
        product_category_name                        AS category_name,
        TRY_CAST(product_name_lenght AS INT)         AS name_length,
        TRY_CAST(product_description_lenght AS INT)  AS description_length,
        TRY_CAST(product_photos_qty AS INT)          AS photos_qty,
        TRY_CAST(product_weight_g AS INT)            AS weight_g,
        TRY_CAST(product_length_cm AS INT)           AS length_cm,
        TRY_CAST(product_height_cm AS INT)           AS height_cm,
        TRY_CAST(product_width_cm AS INT)            AS width_cm,
        _loaded_at::TIMESTAMP_NTZ                    AS _loaded_at
    FROM source

)

SELECT * FROM renamed
