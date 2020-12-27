import hashlib
from cabins.core.cache import get_cached_class
from django.conf import settings
from django.contrib.auth import get_user_model

from .fixtures.core_fixtures import image, site, users, wagtail_site  # noqa
from .fixtures.request import HostNameRequestFactory as rf  # noqa

Site = get_cached_class(settings.CORE_SITE_FINDER).get_model()
User = get_user_model()


def test_create_superuser(db):
    user = User.objects.create_superuser(email="test@test.com", password="this_is_not_a_password")
    assert user.is_superuser is True
    assert user.is_active is True
    assert isinstance(user, User)


def test_create_user(db):
    user = User.objects.create_user(email="test@test.com", password="this_is_not_a_password")
    assert user.is_superuser is False
    assert user.is_active is True
    assert isinstance(user, User)


def test_create_user_no_email(db):
    try:
        User.objects.create_user(email=None, password="this_is_not_a_password")
    except ValueError:
        assert True


def test_create_superuser_not_staff(db):
    try:
        User.objects.create_superuser(email="test@test.com", password="this_is_not_a_password", is_staff=False)
    except ValueError:
        assert True


def test_create_superuser_not_is_superuser(db):
    try:
        User.objects.create_superuser(email="test@test.com", password="this_is_not_a_password", is_superuser=False)
    except ValueError:
        assert True


def test_user_hash(db, users): # noqa
    user = User.objects.get(email="test@test.com")
    assert user.hash == hashlib.sha256("{email}-{date_joined}-{salt}".format(
        email=user.email,
        date_joined=user.date_joined,
        salt=user.salt
    ).encode()).hexdigest()


def test_user_str_rep(db, users): # noqa
    user = User.objects.get(email="test@test.com")
    assert user.email == user.__str__()


def test_core_wagtail_site_utils(db, wagtail_site): # noqa
    SiteUtils = get_cached_class(settings.CORE_SITE_FINDER)
    request = rf(host_name="test.com").get("/")
    site_model = SiteUtils.get_site(request)
    assert site_model.hostname == "test.com"
    assert "wagtailcore.Site" == SiteUtils.get_model()._meta.label


def test_core_site_utils(db, site): # noqa
    SiteUtils = get_cached_class("cabins.core.utils:SiteUtils")
    request = rf(host_name="test.com").get("/")
    site_model = SiteUtils.get_site(request)
    assert site_model.domain == "test.com"
    assert "sites.Site" == SiteUtils.get_model()._meta.label
