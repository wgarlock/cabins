import os
import pytest
from django.core.files import File

from cabins.core import get_image_model_string, get_model
from cabins.page.models import BasePage

image_fixture = dict(
    name="test_image",
    file=os.path.join(os.getcwd(), "cabins-app", "cabins_test", "test_static", "noimage.jpg")
)

Image = get_model(get_image_model_string())


@pytest.fixture
def image(db) -> Image:
    with open(image_fixture["file"], 'rb') as _file:
        file_data = File(_file)
        image = Image(title="test_base")
        image.file.save(
            name="test_base",
            content=file_data
        )
        image.save()


@pytest.fixture
def BasePageFixture(db, image) -> BasePage:
    return BasePage.objects.create(
        description="base_page",
        meta_description="base_page",
        og_description="base_page",
        og_image=Image.objects.get(title="test_base")
    )
