WITH source AS (

    SELECT * FROM {{ source('raw', 'geolocation') }}

),

renamed AS (

    SELECT
        geolocation_zip_code_prefix                AS zip_code,
        TRY_CAST(geolocation_lat AS NUMBER(8,6))   AS latitude,
        TRY_CAST(geolocation_lng AS NUMBER(9,6))   AS longitude,
        LOWER(TRIM(geolocation_city))              AS city,
        UPPER(TRIM(geolocation_state))             AS state,
        _loaded_at::TIMESTAMP_NTZ                  AS _loaded_at
    FROM source

)

SELECT * FROM renamed
