from aws_s3.handlers.s3_handler import S3Handler
from aws_s3.config.cfg import (
    AWS_S3_BUCKET_NAME,
    REGION_NAME,
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
)


def main():
    s3 = S3Handler(
        region_name=REGION_NAME,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )
    s3.create_bucket(bucket_name=AWS_S3_BUCKET_NAME)


if __name__ == "__main__":
    main()
