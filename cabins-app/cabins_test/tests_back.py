from django.contrib.auth.models import AnonymousUser
from django.test import override_settings
from wagtail.images.models import Image

from cabins.back.models import HomePage
from cabins.back.utils import ImageUtils
from cabins.core.exceptions import MisconfiguredModel
from cabins.front.middleware import add_site_context

from .fixtures.back_fixtures import home_page, wagtail_image  # noqa
from .fixtures.request import HostNameRequestFactory as rf


def test_page_context(db, wagtail_image, home_page): # noqa
    request = rf(host_name="test.com").get("/")
    request.user = AnonymousUser()
    request = add_site_context(request)
    home_page = HomePage.objects.get(title="test_home")
    assert home_page.title == "test_home"
    context = home_page.get_context(request=request)
    assert isinstance(context, dict)
    assert context.get("base_context", None) is not None
    assert isinstance(context["base_context"]["page"], dict)
    assert isinstance(context["base_context"]["site_content"], dict)
    assert context["base_context"].get("scheme", None) == "http"
    assert context["base_context"].get("is_authenticated", None) is False


def test_page_serializer(db, wagtail_image, home_page): # noqa
    request = rf(host_name="test.com").get("/")
    request.user = AnonymousUser()
    request = add_site_context(request)
    home_page = HomePage.objects.get(title="test_home")
    assert home_page.title == "test_home"
    home_page.serialize()
    home_page.serialize_all()


def test_core_image_utils(db, wagtail_image): # noqa
    image = Image.objects.get(title="test_home")
    repre = ImageUtils.representation(image)
    assert repre["pk"] == image.pk
    assert repre["url"] == image.file.url
    assert repre["jpeg_400_url"] == image.get_rendition('width-400|format-jpeg').url
    assert repre["jpeg_800_url"] == image.get_rendition('width-800|format-jpeg').url
    assert repre["jpeg_1960_url"] == image.get_rendition('width-1960|format-jpeg').url


@override_settings(CORE_IMAGE_MODEL="cabinscore.Image")
def test_core_image_utils_wrong_model(db, wagtail_image): # noqa
    image = Image.objects.get(title="test_home")
    try:
        ImageUtils.representation(image)
    except MisconfiguredModel:
        assert True
