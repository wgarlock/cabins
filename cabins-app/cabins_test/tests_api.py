from graphene.test import Client

from cabins.api.schema import schema
from cabins.back.models import ContinentalPage, HomePage, ListingPage, RegionalPage, StatePage
from cabins.front.models import SiteContent

from .fixtures.back_fixtures import (  # noqa
    continental_page, home_page, listing_page, region_page, state_page, wagtail_image
)
from .fixtures.front_fixtures import image, site, site_content, social_media  # noqa


def test_all_site_contents(db, image, site, site_content, social_media): # noqa
    client = Client(schema)
    executed = client.execute("""query {
            allSiteContents {
                id
            }
        }
        """)
    assert executed == {'data': {'allSiteContents': [{'id': '1'}]}}


def test_no_home_page(db): # noqa
    client = Client(schema)
    executed = client.execute("""query {
            getHomePageById (id: 2) {
                id
            }
        }
        """)
    assert executed == {'data': {'getHomePageById': None}}


def test_no_regional_page(db): # noqa
    client = Client(schema)
    executed = client.execute("""query {
            getRegionalPageById (id: 2) {
                id
            }
        }
        """)
    assert executed == {'data': {'getRegionalPageById': None}}


def test_no_state_page(db): # noqa
    client = Client(schema)
    executed = client.execute("""query {
            getStatePageById (id: 2) {
                id
            }
        }
        """)
    assert executed == {'data': {'getStatePageById': None}}


def test_no_continental_page(db): # noqa
    client = Client(schema)
    executed = client.execute("""query {
            getContinentalPageById (id: 2) {
                id
            }
        }
        """)
    assert executed == {'data': {'getContinentalPageById': None}}


def test_no_listing_page(db): # noqa
    client = Client(schema)
    executed = client.execute("""query {
            getListingPageById (id: 2) {
                id
            }
        }
        """)
    assert executed == {'data': {'getListingPageById': None}}


def test_no_site_content(db): # noqa
    client = Client(schema)
    executed = client.execute("""query {
            getSiteContentById (id: 2) {
                id
            }
        }
        """)
    assert executed == {'data': {'getSiteContentById': None}}


def test_site_content_serialize(db, image, site, site_content, social_media): # noqa
    content = SiteContent.objects.first().serialize()
    assert 'errors' not in content
    content = SiteContent.objects.first().serialize_all()
    assert 'errors' not in content


def test_home_page_serialize(db, wagtail_image, home_page): # noqa
    content = HomePage.objects.first().serialize()
    assert 'errors' not in content
    content = HomePage.objects.first().serialize_all()
    assert 'errors' not in content


def test_continental_page_serialize(db, wagtail_image, home_page, continental_page): # noqa
    content = ContinentalPage.objects.first().serialize()
    assert 'errors' not in content
    content = ContinentalPage.objects.first().serialize_all()
    assert 'errors' not in content


def test_state_page_serialize(db, wagtail_image, home_page, continental_page, state_page): # noqa
    content = StatePage.objects.first().serialize()
    assert 'errors' not in content
    content = StatePage.objects.first().serialize_all()
    assert 'errors' not in content


def test_region_page_serialize(db, wagtail_image, home_page, continental_page, state_page, region_page): # noqa
    content = RegionalPage.objects.first().serialize()
    assert 'errors' not in content
    content = RegionalPage.objects.first().serialize_all()
    assert 'errors' not in content


def test_listing_page_serialize(db, wagtail_image, home_page, continental_page, state_page, region_page, listing_page): # noqa
    content = ListingPage.objects.first().serialize()
    assert 'errors' not in content
    content = ListingPage.objects.first().serialize_all()
    assert 'errors' not in content
