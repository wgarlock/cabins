import os
import pytest
from cabins.core.cache import get_cached_class
from cabins.core.models import Image
from cabins.page import get_page_string
from django.apps import apps
from django.contrib.auth import get_user_model
from django.core.files import File

Page = apps.get_model(get_page_string())
User = get_user_model()

users_fixture = [
    dict(
        email="test@test.com",
        password="this_is_not_a_password"
    ),
    dict(
        email="test2@test.com",
        password="this_is_not_a_password"
    ),
    dict(
        email="test3@test.com",
        password="this_is_not_a_password"
    ),
    dict(
        email="test4@test.com",
        password="this_is_not_a_password"
    ),
    dict(
        email="test5@test.com",
        password="this_is_not_a_password"
    )
]

site_fixture = [
    dict(
        hostname="test.com",
        site_name="testing"
    )
]

image_fixture = dict(
    name="test_image",
    file=os.path.join(os.getcwd(), "cabins-app", "cabins_test", "test_static", "noimage.jpg")
)


@pytest.fixture
def users(db) -> User:
    return [User.objects.create_user(**user) for user in users_fixture]


@pytest.fixture
def site(db):
    Site = get_cached_class("cabins.core.utils:SiteUtils").get_model()
    return Site.objects.create(
        domain="test.com",
        name="testing",
    )


@pytest.fixture
def wagtail_site(db):
    Site = get_cached_class("cabins.back.utils:SiteUtils").get_model()
    return Site.objects.create(
        hostname="test.com",
        site_name="testing",
        root_page=Page.objects.get(depth=1)
    )


@pytest.fixture
def image(db) -> Image:
    with open(image_fixture["file"], 'rb') as _file:
        file_data = File(_file)
        image = Image(name=image_fixture["name"])
        image.file.save(
            name=image_fixture["name"],
            content=file_data
        )
        image.save()
