from django.contrib.auth.models import AnonymousUser
from django.test import override_settings

from cabins import __version__ as cabins_version
from cabins.back.models import HomePage
from cabins.core.exceptions import MisconfiguredModel
from cabins.front.context_processors import site_content
from cabins.front.templatetags.base import context_dump, static_version

from .fixtures.back_fixtures import home_page, wagtail_image  # noqa
from .fixtures.core_fixtures import site  # noqa
from .fixtures.request import HostNameRequestFactory as rf  # noqa


def test_site_content_context_processor(db, site): # noqa
    request = rf(host_name="test.com").get("/")
    request.user = AnonymousUser()
    site_content(request)
    # check that the cache runs
    site_content(request)


@override_settings(CORE_SITE_MODEL="sites.Site")
def test_add_site_contexts_context_processor_wrong_site(db, site): # noqa
    request = rf(host_name="test.com").get("/")
    request.user = AnonymousUser()
    try:
        request = site_content(request)
    except MisconfiguredModel:
        assert True


def test_template_tag_context_dump(db, wagtail_image, home_page): # noqa
    request = rf(host_name="test.com").get("/")
    request.user = AnonymousUser()
    base_context = site_content(request)
    home_page = HomePage.objects.get(title="test_home")
    assert home_page.title == "test_home"
    context = home_page.get_context(request=request)
    context_dump("context", base_context, context["page_context"])


def test_template_tag_static_version(): # noqa
    static = static_version('cabins-front.css')
    assert cabins_version in static
