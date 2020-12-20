import os
import pytest
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.core.files import File

from cabins.core.models import Image

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
        domain="test.com",
        name="testing"
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
def sites(db) -> Site:
    return [Site.objects.create(**site) for site in site_fixture]


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
