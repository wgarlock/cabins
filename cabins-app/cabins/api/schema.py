import graphene
from django.apps import apps
from django.conf import settings
from graphene_django import DjangoObjectType
from graphene_django.converter import convert_django_field
from taggit.managers import TaggableManager
from wagtail.core.models import Page

from cabins.back.models import ContinentalPage, HomePage, ListingImages, ListingPage, RegionalPage, StatePage
from cabins.front.models import SiteContent, SocialMedia
from cabins.page.models import (
    Activities, FoodDrink, General, NearbyCity, NearByWater, OpenDates, PropertySize, Room, Services, Suitability
)


# convert TaggableManager to string representation
@convert_django_field.register(TaggableManager)
def convert_field_to_string(field, registry=None):
    return graphene.String(description=field.help_text, required=not field.null)


class PageType(DjangoObjectType):
    class Meta:
        model = Page
        fields = "__all__"

    content_type = graphene.String()
    url = graphene.String()

    def resolve_content_type(self, info):
        return self.specific.__class__.__name__

    def resolve_url(self, info):
        return self.url


class SocialMediaType(DjangoObjectType):
    class Meta:
        model = SocialMedia
        fields = "__all__"


class SiteContentType(DjangoObjectType):
    class Meta:
        model = SiteContent
        fields = "__all__"

    navigation = graphene.List(of_type=PageType)
    social_media = graphene.List(of_type=SocialMediaType)

    def resolve_navigation(self, info):
        return self.navigation.all()

    def resolve_social_media(self, info):
        return self.social_media.all()


class HomePageType(DjangoObjectType):
    class Meta:
        model = HomePage
        fields = "__all__"


class ContinentalPageType(DjangoObjectType):
    class Meta:
        model = ContinentalPage
        fields = "__all__"


class StatePageType(DjangoObjectType):
    class Meta:
        model = StatePage
        fields = "__all__"


class RegionalPageType(DjangoObjectType):
    class Meta:
        model = RegionalPage
        fields = "__all__"


class ImageType(DjangoObjectType):
    class Meta:
        model = apps.get_model(settings.CORE_IMAGE_MODEL)
        fields = "__all__"

    url = graphene.String()
    jpeg_400 = graphene.String()
    jpeg_800 = graphene.String()
    jpeg_1960 = graphene.String()

    def resolve_url(self, info):
        return self.file.url

    def resolve_jpeg_400(self, info):
        return self.get_rendition('width-400|format-jpeg').url

    def resolve_jpeg_800(self, info):
        return self.get_rendition('width-800|format-jpeg').url

    def resolve_jpeg_1960(self, info):
        return self.get_rendition('width-1960|format-jpeg').url


class ListingPageType(DjangoObjectType):
    class Meta:
        model = ListingPage
        fields = "__all__"


class ListingImagesType(DjangoObjectType):
    class Meta:
        model = ListingImages
        fields = "__all__"


class OpenDatesType(DjangoObjectType):
    class Meta:
        model = OpenDates
        fields = "__all__"


class GeneralType(DjangoObjectType):
    class Meta:
        model = General
        fields = "__all__"


class FoodDrinkType(DjangoObjectType):
    class Meta:
        model = FoodDrink
        fields = "__all__"


class PropertySizeType(DjangoObjectType):
    class Meta:
        model = PropertySize
        fields = "__all__"


class RoomType(DjangoObjectType):
    class Meta:
        model = Room
        fields = "__all__"


class NearbyCityType(DjangoObjectType):
    class Meta:
        model = NearbyCity
        fields = "__all__"


class ActivitiesType(DjangoObjectType):
    class Meta:
        model = Activities
        fields = "__all__"


class NearByWaterType(DjangoObjectType):
    class Meta:
        model = NearByWater
        fields = "__all__"


class ServicesType(DjangoObjectType):
    class Meta:
        model = Services
        fields = "__all__"


class SuitabilityType(DjangoObjectType):
    class Meta:
        model = Suitability
        fields = "__all__"


class Query(graphene.ObjectType):
    all_site_contents = graphene.List(SiteContentType)
    get_site_content_by_id = graphene.Field(SiteContentType, id=graphene.Int(required=True))
    all_home_pages = graphene.List(HomePageType)
    get_home_page_by_id = graphene.Field(HomePageType, id=graphene.Int(required=True))
    all_continental_pages = graphene.List(ContinentalPageType)
    get_continental_page_by_id = graphene.Field(ContinentalPageType, id=graphene.Int(required=True))
    all_state_pages = graphene.List(StatePageType)
    get_state_page_by_id = graphene.Field(StatePageType, id=graphene.Int(required=True))
    all_regional_pages = graphene.List(RegionalPageType)
    get_regional_page_by_id = graphene.Field(RegionalPageType, id=graphene.Int(required=True))
    all_listing_pages = graphene.List(ListingPageType)
    get_listing_page_by_id = graphene.Field(ListingPageType, id=graphene.Int(required=True))

    def resolve_all_site_contents(self, info):
        # We can easily optimize query count in the resolve method
        return SiteContent.objects.all()

    def resolve_get_site_content_by_id(self, info, id):
        try:
            return SiteContent.objects.select_related("logo").prefetch_related("navigation").get(id=id)
        except SiteContent.DoesNotExist:
            return None

    def resolve_all_home_pages(self, info):
        # We can easily optimize query count in the resolve method
        return HomePage.objects.select_base_related().all()

    def resolve_get_home_page_by_id(self, info, id):
        try:
            return HomePage.objects.select_base_related().get(id=id)
        except HomePage.DoesNotExist:
            return None

    def resolve_all_continental_pages(self, info):
        # We can easily optimize query count in the resolve method
        return ContinentalPage.objects.select_base_related().all()

    def resolve_get_continental_page_by_id(self, info, id):
        try:
            return ContinentalPage.objects.select_base_related().get(id=id)
        except ContinentalPage.DoesNotExist:
            return None

    def resolve_all_state_pages(self, info):
        # We can easily optimize query count in the resolve method
        return StatePage.objects.select_base_related().all()

    def resolve_get_state_page_by_id(self, info, id):
        try:
            return StatePage.objects.select_base_related().get(id=id)
        except StatePage.DoesNotExist:
            return None

    def resolve_all_regional_pages(self, info):
        # We can easily optimize query count in the resolve method
        return RegionalPage.objects.select_base_related().all()

    def resolve_get_regional_page_by_id(self, info, id):
        try:
            return RegionalPage.objects.select_base_related().get(id=id)
        except RegionalPage.DoesNotExist:
            return None

    def resolve_all_listing_pages(self, info):
        # We can easily optimize query count in the resolve method
        return ListingPage.objects.select_base_related().all()

    def resolve_get_listing_page_by_id(self, info, id):
        try:
            return ListingPage.objects.select_base_related().get(id=id)
        except ListingPage.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)
