"""
upload_to_s3.py

Uploads all Olist CSV files from the local `data/` directory to S3 under `olist/`.
Credentials and bucket info are loaded from a `.env` file.

Usage:
    uv run python ingestion/upload_to_s3.py
"""

import os
from pathlib import Path

import boto3
from botocore.exceptions import BotoCoreError, ClientError
from dotenv import load_dotenv

# Load environment variables from .env into memory
load_dotenv()

# AWS credentials and S3 configuration
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

# Path to the local data folder containing the CSV files
DATA_DIR = Path(__file__).parent.parent / "data"

# Create the S3 client using the loaded credentials
s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION,
)

# # Validate that the bucket exists and is accessible before uploading
try:
    s3_client.head_bucket(Bucket=S3_BUCKET_NAME)
    print(f"Access to bucket '{S3_BUCKET_NAME}' validated.")
except (BotoCoreError, ClientError) as e:
    print(e)
    raise SystemExit(1)

# Upload each  CSV file to S3 under olist/
for file in sorted(DATA_DIR.glob("*.csv")):
    key = f"olist/{file.name}"
    try:
        s3_client.upload_file(str(file), S3_BUCKET_NAME, key)
        print(f"Uploaded {file.name} → s3://{S3_BUCKET_NAME}/{key}")
    except (BotoCoreError, ClientError) as e:
        print(f"Failed to upload {file.name}: {e}")