USE SCHEMA olist.raw;

CREATE TABLE geolocation (
    geolocation_zip_code_prefix VARCHAR,
    geolocation_lat VARCHAR,
    geolocation_lng VARCHAR,
    geolocation_city VARCHAR,
    geolocation_state VARCHAR,
    _loaded_at TIMESTAMP_LTZ,
    _source_file VARCHAR,
    _file_row_number INTEGER,
    _file_last_modified TIMESTAMP_NTZ
);
