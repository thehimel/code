import boto3
from botocore.exceptions import ClientError
from utilities.logger import logging


class S3Handler:
    def __init__(self, region_name, aws_access_key_id, aws_secret_access_key):
        self.region_name = region_name
        self.resource = boto3.resource(
            "s3",
            region_name=region_name,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
        )

    def create_bucket(self, bucket_name: str):
        buckets = [bucket.name for bucket in self.resource.buckets.all()]
        if bucket_name in buckets:
            logging.info(msg=f"Bucket {bucket_name} already exists in this account.")
            return

        try:
            self.resource.create_bucket(Bucket=bucket_name)
            logging.info(msg=f"Successfully created the bucket {bucket_name}.")
        except ClientError as e:
            logging.error(msg=f"Error creating bucket {bucket_name}: {e}")
