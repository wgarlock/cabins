import importlib

from django.core.cache import cache


def get_cached_class(cache_key):
    cache_value = cache.get(cache_key, None)
    if cache_value:
        return cache_value

    cache_value = get_class(cache_key)
    cache.set(cache_key, cache_value)
    return cache_value


def get_class(path):
    [module_path, class_str] = path.split(':')
    module = importlib.import_module(module_path)
    return getattr(module, class_str)
