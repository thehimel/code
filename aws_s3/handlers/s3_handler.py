import boto3
from pathlib import Path
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
            logging.info(
                msg=f"s3://{bucket_name}: Bucket already exists in this account."
            )
            return

        try:
            self.resource.create_bucket(Bucket=bucket_name)
            logging.info(msg=f"s3://{bucket_name}: Successfully created the bucket.")
        except ClientError as e:
            logging.error(msg=f"s3://{bucket_name}: Error creating bucket: {e}")

    def upload_file(self, bucket_name: str, local_path: str, remote_path: str):
        try:
            self.resource.Bucket(bucket_name).upload_file(local_path, remote_path)
            logging.info(
                msg=f"s3://{bucket_name}: Successfully uploaded the file to '{remote_path}'."
            )
        except ClientError as e:
            logging.error(msg=f"s3://{bucket_name}: Error uploading file: {e}")

    def copy_file(
        self,
        source_bucket_name: str,
        source_key: str,
        destination_bucket_name: str,
        destination_key: str,
    ):
        try:
            source = {"Bucket": source_bucket_name, "Key": source_key}
            self.resource.Bucket(destination_bucket_name).copy(source, destination_key)
            logging.info(
                msg=f"Successfully copied data from 's3://{source_bucket_name}/{source_key}' "
                f"to 's3://{destination_bucket_name}/{destination_key}'"
            )
        except ClientError as e:
            logging.error(
                msg=f"Error copying data from 's3://{source_bucket_name}/{source_key}'"
                f" to 's3://{destination_bucket_name}/{destination_key}': {e}"
            )

    def download_file(self, bucket_name: str, local_path: str, remote_path: str):
        try:
            self.resource.Bucket(bucket_name).download_file(remote_path, local_path)
            logging.info(
                msg=f"s3://{bucket_name}: Successfully downloaded file to '{local_path}'."
            )
        except ClientError as e:
            logging.error(
                msg=f"s3://{bucket_name}: Error downloading file '{remote_path}': {e}"
            )

    def delete_files(self, bucket_name: str, remote_paths: list[str]):
        remote_objects = [{"Key": remote_path} for remote_path in remote_paths]
        try:
            self.resource.Bucket(bucket_name).delete_objects(
                Delete={"Objects": remote_objects}
            )
            logging.info(
                msg=f"s3://{bucket_name}: Successfully deleted files {remote_paths}."
            )
        except ClientError as e:
            logging.error(msg=f"s3://{bucket_name}: Error deleting files.: {e}")

    def list_files(self, bucket_name: str):
        res = self.resource.meta.client.list_objects(Bucket=bucket_name)
        objects = [content["Key"] for content in res.get("Contents", [])]
        logging.info(msg=f"s3://{bucket_name}: Files = {objects}")

    def upload(self, bucket_name, local_path: str, s3_prefix: str = ""):
        local_path = Path(local_path).resolve()
        if not local_path.is_dir():
            remote_path = s3_prefix + local_path.as_posix()
            self.upload_file(bucket_name=bucket_name, local_path=local_path.as_posix(), remote_path=remote_path)
        for item in local_path.glob('**/*'):
            if item.is_file():
                remote_path = s3_prefix + item.relative_to(local_path).as_posix()
                self.upload_file(bucket_name=bucket_name, local_path=item.as_posix(), remote_path=remote_path)
