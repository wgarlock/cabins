from django.db import models
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase

from cabins.core import get_image_model_string
from cabins.core.models import SeriailizerMixin
from cabins.page import get_page_string


class AbstractBasePage(SeriailizerMixin):
    def context_builder(self, request):
        return {"page": self}

    def get_context_data(self):
        return self.context_builder(self.request)

    def get_context(self, request):
        self.request = request
        self.context = self.get_context_data()
        return self.context


class BasePage(AbstractBasePage, models.Model):
    description = models.TextField()
    meta_description = models.CharField(max_length=120, blank=True, null=True)
    og_description = models.CharField(max_length=300, blank=True, null=True)
    og_image = models.ForeignKey(
        get_image_model_string(), null=True, on_delete=models.SET_NULL, related_name='+'
    )

    serialize_attrs = """
        id
    """


class OpenDates(TaggedItemBase):
    content_object = ParentalKey(get_page_string(), on_delete=models.CASCADE, related_name='amenities_open_dates_tags')


class General(TaggedItemBase):
    content_object = ParentalKey(get_page_string(), on_delete=models.CASCADE, related_name='amenities_general_tags')


class FoodDrink(TaggedItemBase):
    content_object = ParentalKey(get_page_string(), on_delete=models.CASCADE, related_name='food_drink_tags')


class PropertySize(TaggedItemBase):
    content_object = ParentalKey(get_page_string(), on_delete=models.CASCADE, related_name='propertysize_tags')


class Room(TaggedItemBase):
    content_object = ParentalKey(get_page_string(), on_delete=models.CASCADE, related_name='room_tags')


class NearbyCity(TaggedItemBase):
    content_object = ParentalKey(get_page_string(), on_delete=models.CASCADE, related_name='nearbycity_tags')


class Activities(TaggedItemBase):
    content_object = ParentalKey(get_page_string(), on_delete=models.CASCADE, related_name='activities_tags')


class NearByWater(TaggedItemBase):
    content_object = ParentalKey(get_page_string(), on_delete=models.CASCADE, related_name='nearbywater_tags')


class Services(TaggedItemBase):
    content_object = ParentalKey(get_page_string(), on_delete=models.CASCADE, related_name='services_tags')


class Suitability(TaggedItemBase):
    content_object = ParentalKey(get_page_string(), on_delete=models.CASCADE, related_name='suitability_tags')
