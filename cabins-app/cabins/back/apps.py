from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

from cabins.back.signal_handlers import register_signal_handlers


class BaseConfig(AppConfig):
    name = 'cabins.back'
    label = 'cabinsback'
    verbose_name = _("cabins Back Admin")

    def ready(self):
        register_signal_handlers()
