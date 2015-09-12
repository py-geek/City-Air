"""
Django settings for allauthdemo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!h8#n5wopc#7zq!_)i=l#t=q)7g0g-+&0!=kxv+*&2b7*xb8bm'

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
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'bootstrap3', # optional module for making bootstrap forms easier

    'allauth',
    'allauth.account',
    'allauth.socialaccount',



    'allauth.socialaccount.providers.google',  # enabled by configure

    #'allauth.socialaccount.providers.dropbox',
    #'allauth.socialaccount.providers.github',
    #'allauth.socialaccount.providers.linkedin',
    # etc


    'allauthdemo.auth',
    'allauthdemo.demo',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'allauthdemo.urls'

WSGI_APPLICATION = 'allauthdemo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'sql679228',                    
    'USER': 'sql679228',                    
    'PASSWORD': 'cW5!vS4!',                
    'HOST': 'sql6.freemysqlhosting.net',                 
    'PORT': '3306',                     
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# Authentication

AUTHENTICATION_BACKENDS = (
    "allauth.account.auth_backends.AuthenticationBackend",
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)

TEMPLATE_DIRS = (
    # allauth templates: you could copy this directory into your
    # project and tweak it according to your needs
    # os.path.join(PROJECT_ROOT, 'templates', 'uniform', 'allauth'),
    # example project specific templates
    os.path.join(BASE_DIR, 'allauthdemo', 'templates', 'plain', 'example'),
    #os.path.join(BASE_DIR, 'allauthdemo', 'templates', 'bootstrap', 'allauth'),
    os.path.join(BASE_DIR, 'allauthdemo', 'templates', 'allauth'),
    os.path.join(BASE_DIR, 'allauthdemo', 'templates'),
)

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

SITE_ID = 1
AUTH_USER_MODEL = 'auth.DemoUser'
LOGIN_REDIRECT_URL = '/member/'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_MIN_LENGTH = 3
# ACCOUNT_EMAIL_VERIFICATION = 'none'  # testing...
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
SOCIALACCOUNT_AUTO_SIGNUP = False  # require social accounts to use the signup form ... I think
# For custom sign-up form:
# http://stackoverflow.com/questions/12303478/how-to-customize-user-profile-when-using-django-allauth
