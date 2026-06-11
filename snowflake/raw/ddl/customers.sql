USE SCHEMA olist.raw;

CREATE TABLE customers (
    customer_id VARCHAR,
    customer_unique_id VARCHAR,
    customer_zip_code_prefix VARCHAR,
    customer_city VARCHAR,
    customer_state VARCHAR,
    _loaded_at TIMESTAMP_LTZ,
    _source_file VARCHAR,
    _file_row_number INTEGER,
    _file_last_modified TIMESTAMP_NTZ
);
