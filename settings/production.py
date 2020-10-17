from .base import *
import sentry_sdk
import os



DEBUG = False
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_SSL_REDIRECT = True

ALLOWED_HOSTS = ['the-bounce-map.herokuapp.com', 'bouncemap.com']

# Extra lookup directories for collectstatic to find static files
STATICFILES_DIRS = (
    BASE_DIR + '/courts/templates/courts/home/assets',
    BASE_DIR + '/courts/templates/courts/map/assets',
    BASE_DIR + '/courts/templates/404/css',
    BASE_DIR + '/courts/templates/500/assets',
)

sentry_sdk.init(
    dsn=os.environ.get('SENTRY_DSN'),
    integrations=[DjangoIntegration()],
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

django_heroku.settings(locals(),databases=False)
