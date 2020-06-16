from .base import *
import os


INSTALLED_APPS += [
    'import_export',
    'courts',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

DATABASES = {
        'default': {
        'ENGINE': os.environ.get('DB_ENGINE'),
        'ENFORCE_SCHEMA': False,
        'NAME': os.environ.get('DB_NAME'),
        'HOST': os.environ.get('DB_HOST')
    }
}
DEBUG = True
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_BROWSER_XSS_FILTER = False
SECURE_CONTENT_TYPE_NOSNIFF = False
X_FRAME_OPTIONS = 'DENY'
SECURE_SSL_REDIRECT = False

