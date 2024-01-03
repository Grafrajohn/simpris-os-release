"""
Django settings for SimprisDj project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

TEMPLATE_DIRS = ('simprisenv/simpris/simpris/simpris/templates',)

TEMPLATE_CONTEXT_PROCESSORS = (
"django.contrib.auth.context_processors.auth",
"django.core.context_processors.debug",
"django.core.context_processors.i18n",
"django.core.context_processors.media",
"django.core.context_processors.static",
"django.core.context_processors.tz",
"django.contrib.messages.context_processors.messages"                       
)

ALLOWED_HOSTS = ['.simpris.com']

ADMIN_ENABLED = False

# Application definition

INSTALLED_APPS = (
    #'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',   
    'simpris.api',
    'simpris.apps.stress',
    'simpris.apps.project',
    'simpris.apps.crm',
    'simpris.apps.event',
    'simpris.apps.complye'
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

BASE_URL_WEB = 'http://www.simpris.com'
BASE_URL_CI = 'https://www.simpris.com'
BASE_URL_DJ = 'https://www.simpris.com'
BASE_URL = 'https://www.simpris.com'
BASE_ADMIN_URL = 'https://www.simpris.com'
BASE_SUB_URL = 'https://www.simpris.com'
BASE_URL_SUBSCRIPTION = 'https://sites.fastspring.com/your-key/'
COOKIE_DOMAIN = '.simpris.com'
API = 'https://www.simpris.com/api/'
LOGGER = 'simpris_web'
LOGOFF = 'https://www.simpris.com/auth/logout'
LOGIN = 'https://www.simpris.com/auth/logon'
SESSION_COOKIE_AGE = 432000 # no of seconds - 5 days
SESSION_COOKIE_SECURE = True

WSGI_APPLICATION = 'simpris.wsgi.application'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
    #'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework.authentication.TokenAuthentication',)    
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework.authentication.BasicAuthentication','rest_framework.authentication.SessionAuthentication',)#,
    #'PAGINATE_BY': 10
}

# this redirects users who have logged into the REST API
LOGIN_REDIRECT_URL = 'https://www.simpris.com/project/home'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

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
#     'filters': {
#         'special': {
#             '()': 'simpris.logging.SpecialFilter',
#             'foo': 'bar',
#         }
#     },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
     },            
#     'handlers': {
#         'null': {
#             'level': 'DEBUG',
#             'class': 'logging.NullHandler',
#         },
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple'
#         },
#         'mail_admins': {
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler',
#             'filters': ['special']
#         }
#     },
    'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': BASE_DIR + "/django_logfile.log",
#                 'maxBytes': 50000,
#                 'backupCount': 2,
                'when': 'midnight',
                'formatter': 'verbose'
            },
            'file_simpris': {
                'level': 'DEBUG',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': BASE_DIR + "/simpris_logfile.log",
#                 'maxBytes': 100000,
#                 'backupCount': 10,
                'when': 'midnight',
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
#         'django.request': {
#             'handlers': ['mail_admins'],
#             'level': 'ERROR',
#             'propagate': False,
#         },
#         'simpris.custom': {
#             'handlers': ['console', 'mail_admins'],
#             'level': 'INFO',
#             'filters': ['special']
#         }
    }
}

# SILENCED_SYSTEM_CHECKS = ['models.E004',
#                           'models.E120'
#                           ]

#TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATE_FORMAT = "Y/m/d"

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'your-sendgrid-user'
EMAIL_HOST_PASSWORD = 'your-sendgrid-password'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_FROM = 'your-email@your-email.com'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    'simprisenv/simpris/simpris/simpris/static/',
)

UPLOAD_DIR = "simprisenv/simpris/simpris/uploads/"

MEDIA_ROOT = os.path.join(BASE_DIR, 'simpris/uploads/')
MEDIA_URL = '/media/'
