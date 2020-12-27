from cabins.core import get_image_model_string
from cabins.core.models import SeriailizerMixin
from cabins.page import get_page_string
from django.core.cache import cache
from django.db import models
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase


class AbstractBasePage(SeriailizerMixin):
    def context_builder(self, request):
        context = dict()
        cache_key = "base_context-{path}-{host}".format(
            path=request.path,
            host=request.get_host()
        )
        context['base_context'] = cache.get(cache_key)
        if not context['base_context']:
            context['base_context'] = dict()
            context['base_context']['scheme'] = request.is_secure() and 'https' or 'http'
            cache.set(cache_key, context['base_context'])

        context['base_context']['is_authenticated'] = request.user.is_authenticated
        context['base_context']['page'] = self.serialize()
        return context

    def get_context_data(self):
        return self.context_builder(self.request)

    def get_context(self, request):
        self.request = request
        context = super().get_context(request)
        context.update(self.get_context_data())
        return context


class BasePage(AbstractBasePage, models.Model):
    description = models.TextField()
    meta_description = models.CharField(max_length=120, blank=True, null=True)
    og_description = models.CharField(max_length=300, blank=True, null=True)
    og_image = models.ForeignKey(
        get_image_model_string(), null=True, on_delete=models.SET_NULL, related_name='+'
    )


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
