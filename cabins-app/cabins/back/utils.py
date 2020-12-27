from wagtail.core.models import Site


class SiteUtils:
    @classmethod
    def get_site(self, request):
        return Site.find_for_request(request)

    @classmethod
    def get_model(self):
        return Site
