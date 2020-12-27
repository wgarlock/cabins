from cabins.back.models import HomePage
from cabins.front.middleware import add_site_context
from django.contrib.auth.models import AnonymousUser

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
