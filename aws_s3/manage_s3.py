from pathlib import Path

from aws_s3.config.cfg import (AWS_ACCESS_KEY_ID, AWS_S3_BUCKET_NAME, AWS_S3_BUCKET_NAME_SECONDARY,
                               AWS_SECRET_ACCESS_KEY, REGION_NAME)
from aws_s3.handlers.s3_handler import S3Handler


def main():
    s3 = S3Handler(
        region_name=REGION_NAME,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )

    s3.create_bucket(bucket_name=AWS_S3_BUCKET_NAME)
    s3.create_bucket(bucket_name=AWS_S3_BUCKET_NAME_SECONDARY)

    local_path = Path("files/sample.txt").absolute()
    remote_path = local_path.name
    s3.upload_file(
        bucket_name=AWS_S3_BUCKET_NAME,
        local_path=str(local_path),
        remote_path=remote_path,
    )

    s3.copy_file(
        source_bucket_name=AWS_S3_BUCKET_NAME,
        source_key=remote_path,
        destination_bucket_name=AWS_S3_BUCKET_NAME_SECONDARY,
        destination_key=remote_path,
    )

    local_path = Path("files/upload.txt").absolute()
    remote_path = local_path.name
    s3.upload_file(
        bucket_name=AWS_S3_BUCKET_NAME,
        local_path=str(local_path),
        remote_path=remote_path,
    )

    local_path = Path("files/download.txt").absolute()
    s3.download_file(
        bucket_name=AWS_S3_BUCKET_NAME,
        local_path=str(local_path),
        remote_path=remote_path,
    )

    s3.delete_files(
        bucket_name=AWS_S3_BUCKET_NAME, remote_paths=[remote_path, "download.txt"]
    )

    s3.list_files(bucket_name=AWS_S3_BUCKET_NAME)


if __name__ == "__main__":
    main()
