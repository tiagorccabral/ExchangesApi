# settings/production.py
from .base import
import dj_database_url

ENVIRONMENT = 'production'
DEBUG = False
ALLOWED_HOSTS = ['']
DATABASES['default'] = dj_database_url.parse(
    'postgres://USER:PASSWORD@HOST:PORT/NAME', conn_max_age=600
)
