USE SCHEMA olist.raw;

CREATE TABLE IF NOT EXISTS products (
    product_id VARCHAR,
    product_category_name VARCHAR,
    product_name_lenght VARCHAR,
    product_description_lenght VARCHAR,
    product_photos_qty VARCHAR,
    product_weight_g VARCHAR,
    product_length_cm VARCHAR,
    product_height_cm VARCHAR,
    product_width_cm VARCHAR,
    _loaded_at TIMESTAMP_LTZ,
    _source_file VARCHAR,
    _file_row_number INTEGER,
    _file_last_modified TIMESTAMP_NTZ
);
