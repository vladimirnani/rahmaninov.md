import os

TIME_ZONE = 'Europe/Bucharest'
LANGUAGE_CODE = 'ru'
USE_I18N = True
USE_L10N = True
SITE_ID = 1
SECRET_KEY = os.environ['SECRET_KEY']
INTERNAL_IPS = ('127.0.0.1', '::1')

ROOT_URLCONF = 'rahmaninov.urls'
WSGI_APPLICATION = 'rahmaninov.wsgi.application'
PROJECT_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), '')

STATICFILES_DIRS = (os.path.join(PROJECT_PATH, 'static'),)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'apps/website/templates/'),
    os.path.join(PROJECT_PATH, 'apps/website/templates/articles'),
    os.path.join(PROJECT_PATH, 'apps/website/templates/tags'),
    os.path.join(PROJECT_PATH, 'apps/website/templates/people'),
    os.path.join(PROJECT_PATH, 'apps/website/templates/base'),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
)

INSTALLED_APPS += (
    'twitter_tag',
    'sorl.thumbnail',
)

INSTALLED_APPS += (
    'rahmaninov.apps.website',
    'rahmaninov.apps.gallery',
    'rahmaninov.apps.achievements',
    'rahmaninov.apps.events',
    'rahmaninov.apps.graduates',
    'rahmaninov.apps.staff',
    'rahmaninov.apps.school',
    'rahmaninov.apps.pupils',
)

# Twitter
OAUTH_TOKENS_HISTORY = False
TWITTER_OAUTH_TOKEN = os.environ['TWITTER_OAUTH_TOKEN']
TWITTER_OAUTH_SECRET = os.environ['TWITTER_OAUTH_SECRET']
TWITTER_CONSUMER_KEY = os.environ['TWITTER_CONSUMER_KEY']
TWITTER_CONSUMER_SECRET = os.environ['TWITTER_CONSUMER_SECRET']

ADMINS = (
    ('Vladimir Nani', 'vladimirnani@gmail.com'),
)
MANAGERS = ADMINS
