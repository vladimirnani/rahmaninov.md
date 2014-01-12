import os
from rahmaninov.settings.base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
SOUTH_AUTO_FREEZE_APP = True
USE_LIVE_DB = True


if USE_LIVE_DB:
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
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'rahmaninov',
            'USER': 'postgres',
            'PASSWORD': os.environ['DEV_DB_PASSWORD'],
            'PORT': 5432,
        },
    }

MEDIA_ROOT = PROJECT_PATH + '/media/'
MEDIA_URL = '/media/'
STATIC_ROOT = ''
STATIC_URL = '/static/'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT': 3600,
    }
}


MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INSTALLED_APPS += (
    'debug_toolbar',
    'south',
)
