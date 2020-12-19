from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BaseConfig(AppConfig):
    name = 'cabins.page'
    label = 'cabinspage'
    verbose_name = _("cabins Page")

    def ready(self):
        from cabins.core.conf import CoreAppConf  # noqa
