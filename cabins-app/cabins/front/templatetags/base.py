import json
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.cache import cache
from django.utils.safestring import mark_safe
from django_jinja import library

from cabins import __version__
from cabins.page.const import page_cache_key


@library.global_function
def context_dump(var, request, base, page):
    data = base
    cache_key = page_cache_key.format(
        path=page.path,
        host=request.get_host()
    )
    page_context_cache = None
    if settings.PAGE_CACHING:
        page_context_cache = cache.get(cache_key)
    if not page_context_cache or not settings.PAGE_CACHING:
        page_context_cache = dict(page=page.serialize())
        if settings.PAGE_CACHING:
            cache.set(cache_key, page_context_cache)
    data.update(page_context_cache)
    data = mark_safe(json.dumps(data))
    return mark_safe(f"<script type='text/javascript'>var {var} = {data}</script>")


@library.global_function
def static_version(path):
    file, extension = path.split(".")
    path = f"{file}.{__version__}.{extension}"
    return staticfiles_storage.url(path)
