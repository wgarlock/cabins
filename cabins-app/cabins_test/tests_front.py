import mock
from cabins.back.models import HomePage
from cabins.core.exceptions import MisconfiguredModel
from cabins.front.middleware import add_site_context, SiteContentMiddleware
from cabins.front.templatetags.base import dump
from django.contrib.auth.models import AnonymousUser
from django.test import override_settings

from .fixtures.back_fixtures import home_page, wagtail_image  # noqa
from .fixtures.core_fixtures import site  # noqa
from .fixtures.request import HostNameRequestFactory as rf  # noqa


def test_site_content_middleware(db, site): # noqa
    get_response = mock.MagicMock()
    request = rf(host_name="test.com").get("/")
    middleware = SiteContentMiddleware(get_response)
    middleware(request)


def test_add_site_context(db, site): # noqa
    request = rf(host_name="test.com").get("/")
    request = add_site_context(request)
    request = add_site_context(request)


@override_settings(CORE_SITE_MODEL="sites.Site")
def test_add_site_contexts_wrong_SITE(db, site): # noqa
    request = rf(host_name="test.com").get("/")
    try:
        request = add_site_context(request)
    except MisconfiguredModel:
        assert True


def test_template_tag_dump(db, wagtail_image, home_page): # noqa
    request = rf(host_name="test.com").get("/")
    request.user = AnonymousUser()
    request = add_site_context(request)
    home_page = HomePage.objects.get(title="test_home")
    assert home_page.title == "test_home"
    context = home_page.get_context(request=request)
    dump(context["base_context"], "base_context", "context")
