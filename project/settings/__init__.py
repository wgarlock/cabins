from project.settings.base import *  # noqa

if DEBUG:  # noqa
    from project.settings.dev import *  # noqa
    INSTALLED_APPS += DEV_APPS # noqa
    MIDDLEWARE += DEV_MIDDLEWARE # noqa
else:
    from project.settings.production import *  # noqa
