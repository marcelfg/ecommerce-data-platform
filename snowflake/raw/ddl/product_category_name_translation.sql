USE SCHEMA olist.raw;

CREATE TABLE IF NOT EXISTS product_category_name_translation (
    product_category_name VARCHAR,
    product_category_name_english VARCHAR,
    _loaded_at TIMESTAMP_LTZ,
    _source_file VARCHAR,
    _file_row_number INTEGER,
    _file_last_modified TIMESTAMP_NTZ
);
