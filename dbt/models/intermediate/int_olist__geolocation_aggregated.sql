WITH geolocation AS (

    SELECT * FROM {{ ref('stg_olist__geolocation') }}

),

exact_deduped AS (

    SELECT
        zip_code,
        latitude,
        longitude,
        city,
        state,
        MAX(_loaded_at) AS _loaded_at
    FROM geolocation
    GROUP BY zip_code, latitude, longitude, city, state

),

aggregated AS (

    SELECT
        zip_code,
        AVG(latitude)::NUMBER(8,6)  AS latitude,
        AVG(longitude)::NUMBER(9,6) AS longitude
    FROM exact_deduped
    GROUP BY zip_code

)

SELECT * FROM aggregated
