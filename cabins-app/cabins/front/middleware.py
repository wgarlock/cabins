from cabins.core import get_app_site_string
from cabins.core.cache import get_cached_class
from cabins.core.exceptions import MisconfiguredModel
from cabins.front.models import SiteContent
from django.conf import settings
from django.core.cache import cache


class SiteContentMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request = add_site_context(request)
        response = self.get_response(request)
        return response


def add_site_context(request):
    site = get_cached_class(settings.CORE_SITE_FINDER).get_site(request)
    if site._meta.label == get_app_site_string():
        site_cache_key = f"{site.pk}-context-{site._meta.label}"
        site_context = cache.get(site_cache_key, None)
        if not site_context:
            site_context, created = SiteContent.objects.get_or_create(site=site)
            site_context = site_context.serialize()
            cache.set(site_cache_key, site_context)

        request.site_context = site_context
        return request

    raise MisconfiguredModel("Misconfigured Settings make sure the Core Site matches site finder")
