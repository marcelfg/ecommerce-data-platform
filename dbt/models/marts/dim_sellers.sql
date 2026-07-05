WITH sellers AS (

    SELECT * FROM {{ ref('int_olist__sellers_enriched') }}

),

final AS (

    SELECT
        seller_id,
        seller_zip_code,
        seller_city,
        seller_state,
        latitude                                                               AS seller_latitude,
        longitude                                                              AS seller_longitude
    FROM sellers

)

SELECT * FROM final