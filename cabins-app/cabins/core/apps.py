from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BaseConfig(AppConfig):
    name = 'cabins.core'
    label = 'cabinscore'
    verbose_name = _("cabins Core")

    def ready(self):
        from cabins.core.conf import CoreAppConf  # noqa
