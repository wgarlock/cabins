
import environ
import os

env = environ.Env(DEBUG=(bool, False))


def optenv(var):
    return env(var, default=None)


proj = environ.Path(__file__) - 2
root = environ.Path(__file__) - 3

BASE_DIR = root()
PROJECT_DIR = proj()

env.read_env(os.path.join(BASE_DIR, '.env'))

DEBUG = True

SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = env('ALLOWED_HOSTS', default='*')

INSTALLED_APPS = [
    'cabins.core',
    'cabins.page',
    'cabins.back',
    'cabins.front',
    'cabins.api',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites'
]

THIRD_PARTY_APPS = [
    'corsheaders',
    'wagtail.contrib.forms',
    'wagtail.contrib.modeladmin',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'wagtail.api.v2',
    'modelcluster',
    'taggit',
    'django_jinja',
    'graphene_django',
    'rest_auth',
    'treebeard',
    'boto3',
    'storages',
]

INSTALLED_APPS += THIRD_PARTY_APPS


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
    'cabins.front.middleware.SiteContentMiddleware'
]

ROOT_URLCONF = 'project.urls'

_TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.template.context_processors.debug",
    "django.template.context_processors.i18n",
    "django.template.context_processors.media",
    "django.template.context_processors.static",
    "django.template.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.template.context_processors.request"
]

TEMPLATES = [
    {
        "BACKEND": "django_jinja.backend.Jinja2",
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        "APP_DIRS": True,
        'NAME': 'jinja2',
        "OPTIONS": {
            "match_extension": ".jinja",
            "newstyle_gettext": True,
            'context_processors': _TEMPLATE_CONTEXT_PROCESSORS,
            "extensions": [
                "jinja2.ext.do",
                "jinja2.ext.loopcontrols",
                "jinja2.ext.with_",
                "jinja2.ext.i18n",
                "jinja2.ext.autoescape",
                "django_jinja.builtins.extensions.CsrfExtension",
                "django_jinja.builtins.extensions.CacheExtension",
                "django_jinja.builtins.extensions.DebugExtension",
                "django_jinja.builtins.extensions.TimezoneExtension",
                "django_jinja.builtins.extensions.UrlsExtension",
                "django_jinja.builtins.extensions.StaticFilesExtension",
                "django_jinja.builtins.extensions.DjangoFiltersExtension",
                'wagtail.core.jinja2tags.core',
                'wagtail.admin.jinja2tags.userbar',
                'wagtail.images.jinja2tags.images',
            ],
        }
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': _TEMPLATE_CONTEXT_PROCESSORS,
        },
    },
]

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

LANGUAGE_CODE = env('LANGUAGE_CODE', default='en-us')

TIME_ZONE = env('TIME_ZONE', default='UTC')

USE_I18N = True

USE_L10N = True

USE_TZ = True


PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

AUTH_USER_MODEL = 'cabinscore.User'

STAFF_PERMISSION_GROUP_NAME = "Staff"

LANGUAGES = (
    ('en', 'English'),
)

WSGI_APPLICATION = 'project.wsgi.application'

WAGTAIL_SITE_NAME = "cabins"

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = env('BASE_URL', default='')

CRISPY_TEMPLATE_PACK = 'bootstrap4'

CORS_ORIGIN_ALLOW_ALL = env('CORS_ORIGIN_ALLOW_ALL', default=True)

MAX_UPLOAD_SIZE = env('MAX_UPLOAD_SIZE', default="104857600")

WAGTAILIMAGES_MAX_UPLOAD_SIZE = env('WAGTAILIMAGES_MAX_UPLOAD_SIZE', default=100 * 1024 * 1024)

WAGTAILAPI_LIMIT_MAX = 48

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

BROKER_URL = env('BROKER_URL', default='redis://localhost:6379')
CELERY_RESULT_BACKEND = env('CELERY_RESULT_BACKEND', default='redis://localhost:6379')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

DB_ROUTER_BLACK_LIST_HOSTNAMES = []

STATIC_URL = 'static/'
MEDIA_URL = 'media/'

CORE_IMAGE_MODEL = "wagtailimages.Image"
CORE_SITE_MODEL = "wagtailcore.Site"
SITE_ID = 1

CORE_PAGE_MODEL = "wagtailcore.Page"
CORE_IMAGE_RENDITION = "cabins.back.utils:ImageUtils"
CORE_SITE_FINDER = "cabins.back.utils:SiteUtils"

GRAPHENE = {
    "SCHEMA": "cabins.api.schema.schema"
}
