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

DEBUG = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
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

PGK = 'key'
BASE_URL_WEB = 'http://127.0.0.1:8000'
BASE_URL_DJ = 'http://127.0.0.1:8000'
BASE_URL = 'http://127.0.0.1:8000'
API = 'http://127.0.0.1:8000/api/'
SESSION_COOKIE_SECURE = False # this must be off for windows

# Test URLs
BASE_URL_TEST_DEV = 'http://127.0.0.1:8000'
BASE_URL_TEST_LIVE = 'https.www.simpris.com'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.mysql', # this points to PyMySQL in _init_.py in root project folder
       'NAME': 'simpris_dev',
       'USER': 'simpris_user',
       'PASSWORD': 'MySQL-password',
       'HOST': 'MySQL-host', # this works fine for XAMPP
       'PORT': '3306',
        # 'OPTIONS': {
        #     'use_pure': True, # this is for mysql-connector only
        # }
   },    
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
    'static/',
)

UPLOAD_DIR = "simpris/uploads/"

MEDIA_ROOT = os.path.join(BASE_DIR, 'simpris/uploads/')
MEDIA_URL = '/media/'

GOOGLE_RECAPTCHA_SECRET_KEY = 'your Google Captcha secret key'
GOOGLE_RECAPTCHA_SITE_KEY = 'your Google Captcha site key'
