USE SCHEMA olist.raw;

CREATE TABLE IF NOT EXISTS sellers (
    seller_id VARCHAR,
    seller_zip_code_prefix VARCHAR,
    seller_city VARCHAR,
    seller_state VARCHAR,
    _loaded_at TIMESTAMP_LTZ,
    _source_file VARCHAR,
    _file_row_number INTEGER,
    _file_last_modified TIMESTAMP_NTZ
);
