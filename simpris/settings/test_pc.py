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
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['C:/Source/simpris/simpris/templates',],
        'APP_DIRS': True,
        'OPTIONS': {
            # ... some options here ...
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request'
            ],
            'debug': True,
        },
    },
]

ALLOWED_HOSTS = ['localhost','127.0.0.1']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'rest_framework',
    'simpris',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'simpris.urls'

PGK = 'key'
BASE_URL_WEB = 'http://127.0.0.1:8000'
BASE_URL_DJ = 'http://127.0.0.1:8000'
BASE_URL = 'http://127.0.0.1:8000'
BASE_URL_SUBSCRIPTION = 'https://sites.fastspring.com/your-key/'
COOKIE_DOMAIN = '.simpris.com'
API = 'http://127.0.0.1:8000/api/'
LOGGER = 'simpris_web'
LOGOFF = 'http://127.0.0.1:8000/auth/logout'
LOGIN = 'http://127.0.0.1:8000/auth/logon'
SESSION_COOKIE_AGE = 432000 # no of seconds - 5 days
SESSION_COOKIE_SECURE = False # this must be off for windows

# Test URLs
BASE_URL_TEST_DEV = 'http://127.0.0.1:8000'
BASE_URL_TEST_LIVE = 'https.www.simpris.com'

WSGI_APPLICATION = 'simpris.wsgi.application'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
    #'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework.authentication.TokenAuthentication',)
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework.authentication.BasicAuthentication','rest_framework.authentication.SessionAuthentication',)#,
    #'PAGINATE_BY': 10
}

# this redirects users who have logged into the REST API
LOGIN_REDIRECT_URL = '/auth/logon'

LOGIN_URL = '/auth/logon/'

DJANGO_SETTINGS_MODULE=os.path.join("simpris.settings_pc_test")

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join("C:\source\simpris\simpris\simpricity_unit_test.db"),
    }
}

# Fixtures
FIXTURE_DIRS = (
   os.path.join(BASE_DIR, 'fixtures'),
)

# Logging 
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
     },
    'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': BASE_DIR + "\django_logfile.log",
                'formatter': 'verbose'
            },
            'file_simpris': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': BASE_DIR + "\simpris_logfile.log",
                'formatter': 'verbose'
            },                 
        },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'simpris': {
            'handlers': ['file_simpris'],
            'level': 'DEBUG',
        },
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATE_FORMAT = "Y/m/d"

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'sendgrid user'
EMAIL_HOST_PASSWORD = 'sendgrid password'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_FROM = 'support@yourdomain.com'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    'simpris/static/',
)

UPLOAD_DIR = "simpris/uploads/"

MEDIA_ROOT = os.path.join(BASE_DIR, 'simpris/uploads/')
MEDIA_URL = '/media/'
