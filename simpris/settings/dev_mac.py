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

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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
                'django.template.context_processors.request',
                # simpris context processors
                'simpris.context_processors.get_base_url',
                'simpris.context_processors.get_subscription_url',
                'simpris.context_processors.get_recaptcha_site_key', 
            ],
            'debug': True,
        },
    },
]

ALLOWED_HOSTS = ['localhost','127.0.0.1']

CSRF_TRUSTED_ORIGINS = ['http://localhost','http://127.0.0.1']

# Application definition

ROOT_URLCONF = 'simpris.urls'

PGK = 'key'
BASE_URL_WEB = 'https://www.simpris.com'
BASE_URL_DJ = 'http://127.0.0.1:8000'
BASE_URL = 'http://127.0.0.1:8000'
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

# this redirects users who have logged into the REST API
LOGIN_REDIRECT_URL = '/auth/logon'

LOGIN_URL = '/auth/logon/'

DJANGO_SETTINGS_MODULE=os.path.join("simpris.settings")

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join("/Source/Simpris/simpris/simpricity_unit_test.db"),
#     }
# }

DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.mysql',
       'NAME': 'simpricity',
       'USER': '<user>',
       'PASSWORD': '<password>',
       'HOST': 'localhost',
       'PORT': '3306',
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

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    'simpris/static/',
)

UPLOAD_DIR = "simpris/uploads/"

MEDIA_ROOT = os.path.join(BASE_DIR,'media/simpris/uploads/')
MEDIA_URL = os.path.join(BASE_DIR,'/uploads/')

GOOGLE_RECAPTCHA_SECRET_KEY = 'your Google Captcha secret key'
GOOGLE_RECAPTCHA_SITE_KEY = 'your Google Captcha site key'
