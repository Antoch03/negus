"""
Django settings for negus project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import ugettext_lazy 


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/


def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_variable("SECRET_KEY")

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    
    "livesync",
    "parler",
    'django.contrib.staticfiles',

    "navigation.apps.NavigationConfig",
    "menu.apps.MenuConfig",    
    "contact.apps.ContactConfig",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware", 
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "livesync.core.middleware.DjangoLiveSyncMiddleware",
    "django.middleware.locale.LocaleMiddleware",
]

ROOT_URLCONF = 'negus.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "django.template.context_processors.i18n",
            ],
        },
    },
]

WSGI_APPLICATION = 'negus.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE   = 'en-us'
LANGUAGES       = (("en", ugettext_lazy("English")),
                   ("fr", ugettext_lazy("French")),)
LOCALE_PATHS    = (os.path.join(BASE_DIR, "locale"),)
USE_I18N        = True
# Localization
USE_L10N        = True
# Time zone support
USE_TZ          = True
TIME_ZONE       = "UTC"
# Available languages - default "en" / we should not hide untranslated content
PARLER_LANGUAGES = {
        None: ({"code":"en"},{"code":"fr"},),
        "default": {"fallbacl":"en", "hide_untranslated":False,}
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL          = "/static/"
STATICFILES_DIRS    = (os.path.join(BASE_DIR, "static"),)


# Email 
EMAIL_BACKEND           = "django.core.mail.backends.console.EmailBackend"
#SERVER_EMAIL            = "contact@django.com"
DEFAULT_FROM_EMAIL      = "antho.3@hotmail.fr"
EMAIL_SUBJECT_PREFIX    = "[Startup Organizer" 
MANAGERS                = (("Us","anthonyrey.simonnot@gmail.com"),)

