from storages.backends.s3boto3 import S3Boto3Storage


class PublicMediaStorage(S3Boto3Storage):
    """
    The `PublicMediaStorage` class is a subclass of `S3Boto3Storage` that specifies the location,
    default ACL, and file overwrite behavior for media files.
    """

    location = "media"
    default_acl = "public-read"
    file_overwrite = False
