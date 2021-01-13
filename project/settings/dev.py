import dj_database_url
import environ
import os

from project.settings import BASE_DIR

env = environ.Env(DEBUG=(bool, False))


def optenv(var):
    return env(var, default=None)


env.read_env(os.path.join(BASE_DIR, '.env'))

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {'default': dj_database_url.config(default=env('DATABASE_URL_DEV', default=''))}


DEV_APPS = [
    "debug_toolbar",
    "django_extensions"
]

DEV_MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

INTERNAL_IPS = [
    '127.0.0.1',
]

SHOW_TOOLBAR_CALLBACK = True

SEO_JS_PRERENDER_URL = 'https://prerender.cabins.dev/'
SEO_JS_PRERENDER_RECACHE_URL = os.path.join(SEO_JS_PRERENDER_URL, "recache")
