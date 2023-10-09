import boto3
from pathlib import Path
from botocore.exceptions import ClientError

from utilities.logger import logging


class S3Handler:
    def __init__(self, region_name: str, aws_access_key_id: str, aws_secret_access_key: str, default_bucket_name: str,
                 default_download_path: str = ""):
        self.region_name = region_name
        self.default_bucket_name = default_bucket_name

        self.resource = boto3.resource(
            "s3",
            region_name=region_name,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
        )

        self.default_download_path = Path(default_download_path)
        if self.default_download_path.suffix:
            self.default_download_path = self.default_download_path.parent
        self.make_directories(self.default_download_path.as_posix())

    @staticmethod
    def make_directories(path: str):
        """
        Make directories in a path under current working directory ignoring the file if exists in the path.
        """
        path = Path(path)

        # If the path has a suffix, grab the path till it's parent which will be a directory.
        if path.suffix:
            path = path.parent

        path.mkdir(parents=True, exist_ok=True)

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

    def upload_file(self, local_path: str, s3_prefix: str = "", s3_key: str = "", bucket_name: str = None):
        if not bucket_name:
            bucket_name = self.default_bucket_name
        s3_prefix = Path(s3_prefix)
        s3_key = s3_prefix / (local_path if not s3_key else s3_key)
        local_path = Path(local_path).resolve()
        try:
            self.resource.Bucket(bucket_name).upload_file(local_path.as_posix(), s3_key.as_posix())
            logging.info(msg=f"s3://{bucket_name}: Successfully uploaded the file to '{s3_key}'.")
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

    def download_file(self, s3_key: str, local_path: str = "", bucket_name: str = None):
        if not bucket_name:
            bucket_name = self.default_bucket_name

        if not local_path:
            local_path = self.default_download_path / s3_key
        self.make_directories(local_path)

        try:
            self.resource.Bucket(bucket_name).download_file(s3_key, local_path)
            logging.info(msg=f"s3://{bucket_name}: Successfully downloaded file to '{local_path}'.")
        except ClientError as e:
            logging.error(msg=f"s3://{bucket_name}: Error downloading file '{s3_key}': {e}")

    def delete_files(self, bucket_name: str, s3_keys: list[str]):
        remote_objects = [{"Key": s3_key} for s3_key in s3_keys]
        try:
            self.resource.Bucket(bucket_name).delete_objects(
                Delete={"Objects": remote_objects}
            )
            logging.info(
                msg=f"s3://{bucket_name}: Successfully deleted files {s3_keys}."
            )
        except ClientError as e:
            logging.error(msg=f"s3://{bucket_name}: Error deleting files.: {e}")

    def list_files(self, bucket_name: str):
        res = self.resource.meta.client.list_objects(Bucket=bucket_name)
        objects = [content["Key"] for content in res.get("Contents", [])]
        logging.info(msg=f"s3://{bucket_name}: Files = {objects}")

    def upload(self, local_path: str, s3_prefix: str = "", s3_key: str = "", bucket_name: str = None):
        if not bucket_name:
            bucket_name = self.default_bucket_name
        local_path = Path(local_path)

        if not local_path.is_dir():
            self.upload_file(
                bucket_name=bucket_name, local_path=local_path.resolve().as_posix(), s3_prefix=s3_prefix, s3_key=s3_key)

        for item in local_path.glob('**/*'):
            if item.is_file():
                if not s3_prefix:
                    s3_prefix = local_path.as_posix()
                s3_key = item.relative_to(local_path).as_posix()
                self.upload_file(
                    bucket_name=bucket_name, local_path=item.as_posix(), s3_prefix=s3_prefix, s3_key=s3_key)
