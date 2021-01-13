from django.contrib.auth.models import AnonymousUser
from django.test import override_settings

from cabins.page.models import BasePage
from cabins_test.fixtures.page_fixtures import BasePageFixture, image  # noqa

from .fixtures.back_fixtures import home_page, wagtail_image  # noqa
from .fixtures.core_fixtures import site  # noqa
from .fixtures.request import HostNameRequestFactory as rf  # noqa


def test_serailizer_mixin(db, BasePageFixture): # noqa
    request = rf(host_name="test.com").get("/")
    request.user = AnonymousUser()
    base_page = BasePage.objects.get(description="base_page")
    base_page.get_context(request=request)


@override_settings(PAGE_CACHING=False)
def test_serailizer_mixin_no_page_cache(db, BasePageFixture): # noqa
    request = rf(host_name="test.com").get("/")
    request.user = AnonymousUser()
    base_page = BasePage.objects.get(description="base_page")
    base_page.get_context(request=request)
