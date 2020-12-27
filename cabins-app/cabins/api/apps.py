from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BaseConfig(AppConfig):
    name = 'cabins.api'
    label = 'cabinsapi'
    verbose_name = _("Cabins API")
