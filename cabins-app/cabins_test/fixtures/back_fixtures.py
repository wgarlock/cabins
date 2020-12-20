import pytest
from django.core.files import File
from wagtail.core.models import Page
from wagtail.images.models import Image

from cabins.back.models import HomePage

from .core_fixtures import image_fixture


@pytest.fixture
def wagtail_image(db) -> Image:
    with open(image_fixture["file"], 'rb') as _file:
        file_data = File(_file)
        image = Image(title="test_home")
        image.file.save(
            name="test_home",
            content=file_data
        )
        image.save()


@pytest.fixture
def home_page(db, wagtail_image) -> HomePage:
    image = Image.objects.get(title="test_home")
    root_page = Page.objects.get(depth=1)
    root_page.add_child(
        instance=HomePage(
            title="test_home",
            description="test home description",
            meta_description="test home meta description",
            og_description="test home og description",
            hero_image=image,
            og_image=image
        )
    )
    root_page.save()
