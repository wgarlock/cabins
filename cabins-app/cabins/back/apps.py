from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BaseConfig(AppConfig):
    name = 'cabins.back'
    label = 'cabinsback'
    verbose_name = _("cabins Back Admin")
