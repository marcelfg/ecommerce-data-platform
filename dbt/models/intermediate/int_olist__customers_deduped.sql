WITH customers AS (

    SELECT * FROM {{ ref('stg_olist__customers') }}

),

deduped AS (

    SELECT *
    FROM customers
    QUALIFY ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY _loaded_at DESC) = 1

)

SELECT * FROM deduped
