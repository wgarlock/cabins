import hashlib
from django.contrib.auth import get_user_model

from cabins.core.cache import get_cached_class
from cabins.core.models import Image
from cabins.core.utils import ImageUtils, SiteUtils

from .fixtures.core_fixtures import image, sites, users  # noqa
from .fixtures.request import HostNameRequestFactory as rf  # noqa

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


def test_core_site_utils(db, sites): # noqa
    request = rf(host_name="test.com").get("/")
    site = SiteUtils.get_site(request)
    assert site.domain == "test.com"


def test_core_image_utils(db, image): # noqa
    image = Image.objects.get(name="test_image")
    repre = ImageUtils.representation(image)
    assert repre["pk"] == image.pk
    assert repre["url"] == image.file.url


def test_get_cached_class():
    cached_class = get_cached_class("cabins.core.utils:ImageUtils")
    cached_class = get_cached_class("cabins.core.utils:ImageUtils")
    assert cached_class is ImageUtils
