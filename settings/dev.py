from .base import *
import os


INSTALLED_APPS += [
    'import_export',
    'courts',
]
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
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
