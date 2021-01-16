from django.contrib.auth.models import AnonymousUser

from cabins.back.models import HomePage

from .fixtures.back_fixtures import home_page, wagtail_image  # noqa
from .fixtures.request import HostNameRequestFactory as rf


def test_page_context(db, wagtail_image, home_page): # noqa
    request = rf(host_name="test.com").get("/")
    request.user = AnonymousUser()
    home_page_obj = HomePage.objects.get(title="test_home")
    assert home_page_obj.title == "test_home"
    context = home_page_obj.get_context(request=request)
    assert isinstance(context, dict)
    assert context.get("page", None) is not None
    assert isinstance(context["page"], HomePage)


def test_page_serializer(db, wagtail_image, home_page): # noqa
    home_page_obj = HomePage.objects.get(title="test_home")
    assert home_page_obj.title == "test_home"
    home_page_obj.serialize()


def test_clear_page_cache_on_save(db, wagtail_image, home_page): # noqa
    home_page_obj = HomePage.objects.get(title="test_home")
    home_page_obj.title = "new title"
    home_page_obj.save()
