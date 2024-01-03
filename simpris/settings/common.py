"""
Django settings for SimprisDj project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

# from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS removed in 1.10
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'django.contrib.sites', only need this for multiple sites
    'rest_framework',
    'rest_framework.authtoken',
    'simpris',
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'simpris.urls'

PGK = 'stripe_key'
# BASE_URL_SUBSCRIPTION = 'https://sites.fastspring.com/your-key'
COOKIE_DOMAIN = '.simpris.com'
LOGGER = 'simpris_web'
SESSION_COOKIE_AGE = 432000 # no of seconds - 5 days

WSGI_APPLICATION = 'simpris.wsgi.application'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework.authentication.BasicAuthentication',
                                       'rest_framework.authentication.SessionAuthentication',
                                       'rest_framework.authentication.TokenAuthentication'),
    'DATETIME_FORMAT': '%Y-%m-%d %H:%M'
}

# this redirects users who have logged into the REST API
LOGIN_REDIRECT_URL = '/auth/logon'

LOGIN_URL = '/auth/logon/'

DJANGO_SETTINGS_MODULE=os.path.join("simpris.settings")

# Fixtures
FIXTURE_DIRS = (
   os.path.join(BASE_DIR, 'fixtures'),
)

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATE_FORMAT = "Y/m/d"

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_FROM = 'yoursupport@youremail.com'
