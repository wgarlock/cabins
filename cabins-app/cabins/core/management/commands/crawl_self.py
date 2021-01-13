import requests
import xml.etree.ElementTree as ET
from django.conf import settings
from django.core.management.base import BaseCommand

from cabins.core import get_app_site_string, get_model


class Command(BaseCommand):
    help = 'Crawl and pre cache the site'

    def handle(self, *args, **options):
        Site = get_model(get_app_site_string())
        sites = Site.objects.all()

        for site in sites:
            host = None
            if hasattr(site, "domain"):
                host = site.domain
            if hasattr(site, "hostname"):
                host = site.hostname
            if host:
                if settings.DEBUG:
                    sitemap = requests.get(f"http://{host}/sitemap.xml/")
                else:
                    sitemap = requests.get(f"https://{host}/sitemap.xml/")
                root = ET.fromstring(sitemap.content)
                for child in root.findall(
                    '{http://www.sitemaps.org/schemas/sitemap/0.9}url/{http://www.sitemaps.org/schemas/sitemap/0.9}loc'
                ):
                    requests.get(f"{settings.SEO_JS_PRERENDER_URL}render?url={child.text}")
