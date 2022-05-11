from storages.backends.s3boto3 import S3Boto3Storage

from Online_Portfolio_and_Blog_With_CMS import settings


class StaticStorage(S3Boto3Storage):
    """Custom storage class for static files."""

    location = settings.STATICFILES_LOCATION

class MediaStorage(S3Boto3Storage):
    """Custom storage class for media files."""

    location = settings.MEDIAFILES_LOCATION