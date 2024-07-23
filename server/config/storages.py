from storages.backends.s3boto3 import S3StaticStorage, S3Boto3Storage


# 사용 시, production.py에서 주석 해제 필요
class StaticStorage(S3StaticStorage):
    location = "static"


class MediaStorage(S3Boto3Storage):
    location = "media"
