"""
Django settings for super project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.conf import global_settings
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)

DEBUG = False

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

gettext = lambda s: s

LANGUAGES = (
    ('en-us', gettext('English')),
)

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Application definition

INSTALLED_APPS = (
    'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'pipeline',
    'pyjade.ext.django',
    'application.accounts',
    'application.api',
    'rest_framework_swagger',
    #'application.ui',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.auth.middleware.RemoteUserMiddleware',
    #'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'pipeline.middleware.MinifyHTMLMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.static',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

ROOT_URLCONF = 'super.urls'

WSGI_APPLICATION = 'super.wsgi.application'

DEFAULT_USER = 'my_user'
DEFAULT_PASS = 'my_password'

SECRET_KEY = 'zj!40s3evq%%(f--xj^w2oybttb1-t3^t8uwn9tc@_7tdm=8ow'

WSGI_APPLICATION = 'super.wsgi.application'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGE_SIZE': 10
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'EXCEPTION_HANDLER': 'application.api.helpers.auth.custom_exception_handler',
}

AUTH_USER_MODEL = 'accounts.User'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

AUTHENTICATION_BACKENDS = (
    'application.api.helpers.auth.MyRemoteUserBackend',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_REDIRECT_URL = '/'

SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_AGE = 5 * 60

# UI templates

TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),)
TEMPLATE_LOADERS = (
    ('pyjade.ext.django.Loader',(
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
        'django.template.loaders.eggs.Loader',
    )),
)

# UI static

STATIC_ROOT = os.path.join('/sockets', 'cache-super/static')
STATIC_URL = '/assets/'

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATIC_DEV = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

#PIPELINE_ENABLED = True
PIPELINE_STORAGE = 'pipeline.storage.PipelineFinderStorage'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.jsmin.JSMinCompressor'
PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.cssmin.CSSMinCompressor'
PIPELINE_COMPILERS = (
    'pipeline.compilers.stylus.StylusCompiler',
    'pipeline.compilers.coffee.CoffeeScriptCompiler',
)

PIPELINE_CSS = {
    'links': {
        'source_filenames': (
            'super_api/styl/*.styl',
            'main/styl/*.styl',
        ),
        'output_filename': os.path.join('css', 'compressed.css'),
        'extra_context': {
            'media': 'screen,projection',
        },
        'variant': 'datauri'
    },
}

PIPELINE_JS = {
    'scripts': {
        'source_filenames': (
            'super_api/coffee/*.coffee',
            'main/js/*.js',
            'main/coffee/*.coffee',
        ),
        'extra_context': {
            'async': True,
        },
        'output_filename': os.path.join('js', 'compressed.js'),
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'stream': sys.stdout
        },
    },
    'loggers': {
        'django': {
            'handlers':['console'],
            'propagate': True,
            'level':'DEBUG',
        },
    }
}
