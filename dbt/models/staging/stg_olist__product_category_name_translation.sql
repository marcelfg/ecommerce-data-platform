WITH source AS (

    SELECT * FROM {{ source('raw', 'product_category_name_translation') }}

),

renamed AS (

    SELECT
        product_category_name          AS product_category_name_pt,
        product_category_name_english  AS product_category_name_en,
        _loaded_at::TIMESTAMP_NTZ      AS _loaded_at
    FROM source

)

SELECT * FROM renamed
