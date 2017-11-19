# -*- coding: utf-8 -*-
"""
Django settings for test_django project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import django

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
VERSION = django.get_version()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_pvb87d0p7%^955rx#&p7+#rl*ln37e(n-)*w%5lthvrd^%(j5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # add by mz
    'gunicorn',
    'test_django'
)

if VERSION == "1.9":

    MIDDLEWARE_CLASSES = (
        'test_django.views.frame_django_test.BlockedIpMiddleware',
        'django.middleware.cache.UpdateCacheMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.middleware.cache.FetchFromCacheMiddleware',
    )
    CACHES = {
        # 'default': {
        #     'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        #     'LOCATION': '127.0.0.1:11211',
        #     'TIMEOUT': 60,
        #     'OPTIONS': {
        #         'MAX_ENTRIES': 1000
        #     }
        # },
        'default': {
            'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
            'LOCATION': '/var/tmp/django_cache',
            'TIMEOUT': 10,
            'OPTIONS': {
                'MAX_ENTRIES': 1000
            }
        },
        # 'default': {
        #     'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        #     'LOCATION': 'unique-snowflake',
        #     'TIMEOUT': 60,
        #     'OPTIONS': {
        #         'MAX_ENTRIES': 10000
        #     }
        # }
    }

elif VERSION == "1.7.11":

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

elif VERSION == "1.6":

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )
elif VERSION == "1.4":

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )




ROOT_URLCONF = 'test_django.urls'

WSGI_APPLICATION = 'test_django.wsgi.application'

# add by mz
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "test_django\\templates").replace('\\', '/'),
   )
# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases


DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },

    'postgresql_psycopg2': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'xiguago',
        'USER': 'tingyun',
        'PASSWORD': 'tingyun',
        'HOST': '192.168.2.43',
        'PORT': '5432'
    },

    'mysql_mysqldb': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'xiguago',
        'USER': 'tingyun',
        'PASSWORD': 'tingyun',
        'HOST': '192.168.2.43',
        'PORT': '3306',
        # 'ATOMIC_REQUESTS': True
    },

    'oracle_cx_oracle': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'nbsdb',
        'USER': 'test',
        'PASSWORD': 'TEST',
        'HOST': '192.168.1.15',
        'PORT': '1521'
    },

    # 'sqlserver_pyodbc': {
    #     'ENGINE': 'sql_server.pyodbc',
    #     'NAME': 'python_test',
    #     'USER': 'leng',
    #     'PASSWORD': 'Windows2008',
    #     'HOST': '192.168.2.200',
    #     'PORT': '1433'
    # }
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'