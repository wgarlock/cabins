import pytest
from cabins.core.cache import get_cached_class
from cabins.front.models import SiteContent, SocialMedia
from cabins.page import get_page_string
from django.apps import apps
from django.conf import settings
from django.core.files import File

from .core_fixtures import image_fixture

Site = get_cached_class(settings.CORE_SITE_FINDER).get_model()
Image = apps.get_model(settings.CORE_IMAGE_MODEL)
Page = apps.get_model(get_page_string())


@pytest.fixture
def image(db) -> Image:
    with open(image_fixture["file"], 'rb') as _file:
        file_data = File(_file)
        image = Image(title="test_home")
        image.file.save(
            name="test_home",
            content=file_data
        )
        image.save()


@pytest.fixture
def site(db) -> Site:
    return Site.objects.create(
        hostname="test.com",
        site_name="test",
        port=8000,
        root_page=Page.objects.filter(depth=1).first()
    )


@pytest.fixture
def site_content(db, image, site) -> SiteContent:
    site_content = SiteContent.objects.create(
        footer_content="test",
        logo=Image.objects.get(title="test_home"),
        site=Site.objects.get(hostname="test.com")
    )
    site_content.navigation.set(Page.objects.filter(depth=1))
    return site_content


@pytest.fixture
def social_media(db, site_content) -> SocialMedia:
    return SocialMedia.objects.create(
        site=SiteContent.objects.get(site__hostname="test.com"),
        name="facebook",
        url="https://facebook.com",
        icon="facebook"
    )
