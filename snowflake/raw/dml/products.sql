COPY INTO olist.raw.products
FROM @olist.raw.s3_olist_stage/olist_products_dataset.csv
FILE_FORMAT = (
    TYPE = 'CSV'
    FIELD_OPTIONALLY_ENCLOSED_BY = '"'
    PARSE_HEADER = TRUE
    ERROR_ON_COLUMN_COUNT_MISMATCH = FALSE
)
MATCH_BY_COLUMN_NAME = CASE_INSENSITIVE
INCLUDE_METADATA = (
    _loaded_at = METADATA$START_SCAN_TIME,
    _source_file = METADATA$FILENAME,
    _file_row_number = METADATA$FILE_ROW_NUMBER,
    _file_last_modified = METADATA$FILE_LAST_MODIFIED
)
ON_ERROR = 'CONTINUE';
