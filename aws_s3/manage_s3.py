from pathlib import Path

from aws_s3.config.cfg import (AWS_ACCESS_KEY_ID, AWS_S3_BUCKET_NAME, AWS_S3_BUCKET_NAME_SECONDARY,
                               AWS_SECRET_ACCESS_KEY, REGION_NAME)
from aws_s3.handlers.s3_handler import S3Handler


def main():
    s3 = S3Handler(
        region_name=REGION_NAME,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        default_bucket_name=AWS_S3_BUCKET_NAME,
        default_download_path="downloads"
    )

    s3.create_bucket(bucket_name=AWS_S3_BUCKET_NAME)
    s3.create_bucket(bucket_name=AWS_S3_BUCKET_NAME_SECONDARY)

    s3.upload_file(local_path="uploads/root.txt")
    s3.upload_file(local_path="uploads/sample.txt")
    s3.upload(local_path="uploads/parent", s3_prefix="root")

    s3.copy_file(
        source_bucket_name=AWS_S3_BUCKET_NAME,
        source_key="files/sample.txt",
        destination_bucket_name=AWS_S3_BUCKET_NAME_SECONDARY,
        destination_key="files/sample.txt",
    )

    s3.download_file(s3_key="files/sample.txt")

    s3.delete_files(
        bucket_name=AWS_S3_BUCKET_NAME, s3_keys=["files/root.txt"]
    )

    s3.list_files(bucket_name=AWS_S3_BUCKET_NAME)


if __name__ == "__main__":
    main()
