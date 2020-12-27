from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site


class SiteUtils:
    @classmethod
    def get_site(self, request):
        return get_current_site(request)

    @classmethod
    def get_model(self):
        return Site
