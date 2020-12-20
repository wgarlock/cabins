from django.contrib.sites.shortcuts import get_current_site


class SiteUtils:
    @classmethod
    def get_site(self, request):
        return get_current_site(request)


class ImageUtils:
    @classmethod
    def representation(self, value):
        return dict(
            pk=value.pk,
            url=value.file.url
        )
