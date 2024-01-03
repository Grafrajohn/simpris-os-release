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
DEBUG = os.environ.get('DEBUG')

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
            'debug': os.environ.get('DEBUG'),
        },
    },
]

ALLOWED_HOSTS = ['localhost','127.0.0.1','web',os.environ.get('BASE_URL')]

CSRF_TRUSTED_ORIGINS = ['https://localhost']

# Application definition

ROOT_URLCONF = 'simpris.urls'

PGK = 'key'
BASE_URL_WEB = 'https://' + os.environ.get('BASE_URL') + os.environ.get('BASE_PORT') 
BASE_URL_DJ = 'https://' + os.environ.get('BASE_URL') + os.environ.get('BASE_PORT') 
BASE_URL = 'https://' + os.environ.get('BASE_URL') + os.environ.get('BASE_PORT') 
BASE_URL_SUBSCRIPTION = 'https://sites.fastspring.com/your-key'
COOKIE_DOMAIN = '.simpris.com'
API = 'https://' + os.environ.get('BASE_URL') + os.environ.get('BASE_PORT')  + '/api/'
LOGGER = 'simpris_web'
LOGOFF = 'https://' + os.environ.get('BASE_URL') + os.environ.get('BASE_PORT')  + '/auth/logout'
LOGIN = 'https://' + os.environ.get('BASE_URL') + os.environ.get('BASE_PORT')  + '/auth/logon'
SESSION_COOKIE_AGE = 432000 # no of seconds - 5 days
SESSION_COOKIE_SECURE = False # this must be off for windows

# Test URLs
BASE_URL_TEST_DEV = 'http://' + os.environ.get('BASE_URL') + os.environ.get('BASE_PORT') 
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
       'NAME': os.environ.get('DB_NAME', "simpricity"),
       'USER': os.environ.get('DB_USER'),
       'PASSWORD': os.environ.get('DB_PASSWORD'),
       'HOST': os.environ.get('DB_HOST'), # docker recommended host
       'PORT': '3306',
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
            'filename': BASE_DIR + "\\django_logfile.log",
            'formatter': 'verbose'
        },
        'file_simpris': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR + "\\simpris_logfile.log",
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

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    'static/',
]

UPLOAD_DIR = "simpris/uploads/"

MEDIA_ROOT = os.path.join(BASE_DIR,'media/simpris/uploads/')
MEDIA_URL = os.path.join(BASE_DIR,'/uploads/')

GOOGLE_RECAPTCHA_SECRET_KEY = os.environ.get('GOOGLE_RECAPTCHA_SECRET_KEY') 
GOOGLE_RECAPTCHA_SITE_KEY = os.environ.get('GOOGLE_RECAPTCHA_SITE_KEY') 
