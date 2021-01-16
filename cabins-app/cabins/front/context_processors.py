from django.conf import settings
from django.core.cache import cache

from cabins.core import get_app_site_string
from cabins.core.cache import get_cached_class
from cabins.front.models import SiteContent


def site_content(request):
    site = get_cached_class(settings.CORE_SITE_FINDER).get_site(request)
    if site._meta.label == get_app_site_string():
        site_cache_key = f"{site.pk}-context-{site._meta.label}"
        site_context = cache.get(site_cache_key)
        if not site_context:
            site_context, created = SiteContent.objects.get_or_create(site=site)
            site_context = site_context.serialize()
            cache.set(site_cache_key, site_context)
        return {
            "base_context": {
                "site_content": site_context,
                "scheme": request.is_secure() and 'https' or 'http',
                "is_authenticated": request.user.is_authenticated
            }
        }
