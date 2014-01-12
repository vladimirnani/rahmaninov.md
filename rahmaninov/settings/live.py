import logging
from rahmaninov.settings.base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG
INSTALLED_APPS += (
    'gunicorn',
)
ALLOWED_HOSTS = [
    '.rahmaninov.md',
    '.rahmaninov-web.herokuapp.com',
]

# MEDIA
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = 'rachmaninoff'
AWS_URL = 'http://s3-eu-west-1.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME
DEFAULT_S3_PATH = 'media'
STATIC_S3_PATH = 'static'
AWS_S3_SECURE_URLS = False
MEDIA_ROOT = '/%s/' % DEFAULT_S3_PATH
MEDIA_URL = AWS_URL + 'media/'
STATIC_ROOT = '/%s/' % STATIC_S3_PATH
STATIC_URL = AWS_URL + 'static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['LIVE_DB_NAME'],
        'HOST': 'ec2-23-23-214-251.compute-1.amazonaws.com',
        'PORT': 5432,
        'USER': os.environ['LIVE_DB_USER'],
        'PASSWORD': os.environ['LIVE_DB_PASSWORD']
    }
}

# CACHE
os.environ['MEMCACHE_SERVERS'] = os.environ.get('MEMCACHIER_SERVERS', '')
os.environ['MEMCACHE_USERNAME'] = os.environ.get('MEMCACHIER_USERNAME', '')
os.environ['MEMCACHE_PASSWORD'] = os.environ.get('MEMCACHIER_PASSWORD', '')
CACHES = {
    'default': {
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
        'BINARY': True,
        'OPTIONS': {
            'tcp_nodelay': True,
            'remove_failed': 4
        }
    }
}

# LOGGING
EMAIL_HOST = os.environ['MAILGUN_SMTP_SERVER']
EMAIL_PORT = os.environ['MAILGUN_SMTP_PORT']
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ['MAILGUN_SMTP_LOGIN']
EMAIL_HOST_PASSWORD = os.environ['MAILGUN_SMTP_PASSWORD']
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
