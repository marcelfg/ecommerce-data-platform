-- Create storage integration between Snowflake and S3
-- Requires ACCOUNTADMIN role to execute
CREATE STORAGE INTEGRATION s3_olist_integration
    TYPE = EXTERNAL_STAGE
    STORAGE_PROVIDER = 'S3'
    ENABLED = TRUE
    STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::612169429581:role/snowflake_s3_olist_role'
    STORAGE_ALLOWED_LOCATIONS = ('s3://ecommerce-data-platform-landing-612169429581-eu-west-2-an/olist/');