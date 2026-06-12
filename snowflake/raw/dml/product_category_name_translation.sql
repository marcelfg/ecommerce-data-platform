COPY INTO olist.raw.product_category_name_translation
FROM @olist.raw.s3_olist_stage/product_category_name_translation.csv
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
