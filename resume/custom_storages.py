from django.conf import settings

if settings.DEBUG:
    from django.core.files.storages import FileSystemStorage

    class MediaStorage(FileSystemStorage):
        fileoverwrite = False
        default_acl = 'public-read'
else:
    from storages.backends.s3boto3 import S3Boto3Storage

    class MediaStorage(S3Boto3Storage):
        fileoverwrite = False
        default_acl = 'public-read'
        location = settings.MEDIA_LOCATION