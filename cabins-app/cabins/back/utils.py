from wagtail.core.models import Site

from cabins.core import get_image_model_string
from cabins.core.exceptions import MisconfiguredModel


class SiteUtils:
    @classmethod
    def get_site(self, request):
        return Site.find_for_request(request)


class ImageUtils:
    @classmethod
    def representation(self, value):
        if value._meta.label == get_image_model_string():
            # TODO make these value a generic value and then create renditions automatically
            # when the file is uploaded to precent latency issues when they are first requested
            return dict(
                pk=value.pk,
                url=value.file.url,
                jpeg_400_url=value.get_rendition('width-400|format-jpeg').url,
                jpeg_800_url=value.get_rendition('width-800|format-jpeg').url,
                jpeg_1960_url=value.get_rendition('width-1960|format-jpeg').url
            )

        raise MisconfiguredModel(
            'Wrong Image Model Implemented. Make sure your CORE_IMAGE_MODEL = '
            '"wagtailimages.Image in settings"'
        )
