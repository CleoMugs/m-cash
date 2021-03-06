import datetime

from decouple import config

AWS_ACCESS_KEY_ID = "AKIARLMIVNP6MNIZF762"  #config("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = "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"#config("AWS_SECRET_ACCESS_KEY")

AWS_FILE_EXPIRE = 200
AWS_S3_FILE_OVERWRITE = False
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = False

AWS_LOCATION = 'static' # temporary
AWS_DEFAULT_ACL = None # temporary

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


#DEFAULT_FILE_STORAGE = 'mpesa.aws.utils.MediaRootS3BotoStorage'
#STATICFILES_STORAGE = 'mpesa.aws.utils.StaticRootS3BotoStorage'


AWS_STORAGE_BUCKET_NAME = 'mpesa-bucket' #config("AWS_STORAGE_BUCKET_NAME")
S3DIRECT_REGION = "eu-west-2"

S3_URL = "//%s.s3.amazonaws.com/" % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = "//%s.s3.amazonaws.com/media/" % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = MEDIA_URL
STATIC_URL = S3_URL + "static/"
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = {
    "Expires": expires,
    "Cache-Control": "max-age=%d" % (int(two_months.total_seconds()),),
}


'''
import datetime

from decouple import config

AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")

AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = False

DEFAULT_FILE_STORAGE = "mpesa.aws.utils.MediaRootS3BotoStorage"
STATICFILES_STORAGE = "mpesa.aws.utils.StaticRootS3BotoStorage"


AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME")
S3DIRECT_REGION = "eu-west-2"

S3_URL = "//%s.s3.amazonaws.com/" % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = "//%s.s3.amazonaws.com/media/" % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = MEDIA_URL
STATIC_URL = S3_URL + "static/"
ADMIN_MEDIA_PREFIX = STATIC_URL + "admin/"

two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS = {
    "Expires": expires,
    "Cache-Control": "max-age=%d" % (int(two_months.total_seconds()),),
}
'''

 