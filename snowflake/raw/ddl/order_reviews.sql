USE SCHEMA olist.raw;

CREATE TABLE order_reviews (
    review_id VARCHAR,
    order_id VARCHAR,
    review_score VARCHAR,
    review_comment_title VARCHAR,
    review_comment_message VARCHAR,
    review_creation_date VARCHAR,
    review_answer_timestamp VARCHAR,
    _loaded_at TIMESTAMP_LTZ,
    _source_file VARCHAR,
    _file_row_number INTEGER,
    _file_last_modified TIMESTAMP_NTZ
);
