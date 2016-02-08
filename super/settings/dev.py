from .base import *
import dj_database_url


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {'default': dj_database_url.config(default='postgres://postgres:postgres@postgres:5432/postgres')}

try:
    from .local import *
except:
    pass