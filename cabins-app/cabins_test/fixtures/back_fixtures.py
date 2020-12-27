import pytest
from cabins.back.models import ContinentalPage, HomePage, ListingPage, RegionalPage, StatePage
from django.core.files import File
from wagtail.core.models import Page
from wagtail.images.models import Image

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


@pytest.fixture
def continental_page(db, wagtail_image, home_page) -> ContinentalPage:
    image = Image.objects.get(title="test_home")
    home_page = HomePage.objects.first()
    home_page.add_child(
        instance=ContinentalPage(
            title="test_continental",
            description="test ontinental description",
            meta_description="test ontinental meta description",
            og_description="test ontinental og description",
            hero_image=image,
            og_image=image
        )
    )
    home_page.save()


@pytest.fixture
def state_page(db, wagtail_image, home_page, continental_page) -> StatePage:
    image = Image.objects.get(title="test_home")
    con_page = ContinentalPage.objects.first()
    con_page.add_child(
        instance=StatePage(
            title="test_state",
            description="test ontinental description",
            meta_description="test ontinental meta description",
            og_description="test ontinental og description",
            hero_image=image,
            og_image=image
        )
    )
    con_page.save()


@pytest.fixture
def region_page(db, wagtail_image, home_page, continental_page, state_page) -> RegionalPage:
    image = Image.objects.get(title="test_home")
    state_page = StatePage.objects.first()
    state_page.add_child(
        instance=RegionalPage(
            title="test_region",
            description="test region description",
            meta_description="test region meta description",
            og_description="test region og description",
            hero_image=image,
            og_image=image
        )
    )
    state_page.save()


@pytest.fixture
def listing_page(db, wagtail_image, home_page, continental_page, state_page, region_page) -> ListingPage:
    image = Image.objects.get(title="test_home")
    reg_page = RegionalPage.objects.first()
    reg_page.add_child(
        instance=ListingPage(
            title="test_listing",
            description="test listing description",
            meta_description="test listing meta description",
            og_description="test listing og description",
            hero_image=image,
            og_image=image,
            street="test1",
            street2="ave",
            city="testcity",
            region="ohio",
            country="usa",
            postal_code="44094",
            website="https://test.com"
        )
    )
    reg_page.save()
