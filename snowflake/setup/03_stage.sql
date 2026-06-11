-- Create external stage pointing to S3 olist folder
USE SCHEMA olist.raw;

CREATE STAGE s3_olist_stage
    STORAGE_INTEGRATION = s3_olist_integration
    URL = 's3://ecommerce-data-platform-landing-612169429581-eu-west-2-an/olist/'
    FILE_FORMAT = (TYPE = 'CSV' FIELD_OPTIONALLY_ENCLOSED_BY = '"' SKIP_HEADER = 1);