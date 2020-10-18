from .base import *
import environ

base = environ.Path(__file__) - 2 # two folders back (/a/b/ - 2 = /)
environ.Env.read_env(env_file=base('.env')) # reading .env file

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Extra lookup directories for collectstatic to find static files
STATICFILES_DIRS = (
    BASE_DIR + '/courts/templates/courts/home/assets',
    BASE_DIR + '/courts/templates/courts/map/assets',
    BASE_DIR + '/courts/templates/404/css',
    BASE_DIR + '/courts/templates/500/assets',
)
