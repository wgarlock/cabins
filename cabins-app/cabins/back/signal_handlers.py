from django.conf import settings
from django.core.cache import caches

from cabins.back.signals import base_page_save
from cabins.page.const import page_cache_key


def clear_page_cache_on_save(sender, instance, **kwargs):
    cache = caches["default"]
    for host in settings.ALLOWED_HOSTS:
        cache.delete(page_cache_key.format(
            path=instance.path,
            host=host
        ))


def register_signal_handlers():
    base_page_save.connect(clear_page_cache_on_save)
