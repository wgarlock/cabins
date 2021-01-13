from django.db import models
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, ObjectList, TabbedInterface
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page, PageManager
from wagtail.images.edit_handlers import ImageChooserPanel

from cabins.core import get_image_model_string
from cabins.core.models import Orderable
from cabins.page.models import AbstractBasePage


class WagtailBasePageManager(PageManager):
    def select_base_related(self):
        return self.select_related("hero_image", "og_image")


class WagtailBasePage(AbstractBasePage, Page):

    description = RichTextField()
    meta_description = models.CharField(max_length=120, blank=True, null=True)
    og_description = models.CharField(max_length=300, blank=True, null=True)
    hero_image = models.ForeignKey(
        get_image_model_string(), null=True, on_delete=models.SET_NULL, related_name='+'
    )
    og_image = models.ForeignKey(
        get_image_model_string(), null=True, on_delete=models.SET_NULL, related_name='+'
    )
    content_panels = Page.content_panels + [
        FieldPanel('description', classname='full'),
        ImageChooserPanel('hero_image'),
    ]
    promote_panels = Page.promote_panels + [
        MultiFieldPanel([
            FieldPanel('meta_description', help_text='in browser text: max chars 120'),
            FieldPanel('og_description', help_text='social media text: max chars 300'),
            ImageChooserPanel('og_image'),
        ], 'Open Graph Content'),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels, heading='Content'),
            ObjectList(promote_panels, heading='SEO'),
            ObjectList(Page.settings_panels, heading='Settings'),
        ]
    )

    objects = WagtailBasePageManager()

    class Meta(Page.Meta):
        abstract = True


class HomePage(WagtailBasePage):
    template = "home_page.jinja"
    subpage_types = [
        'cabinsback.ContinentalPage'
    ]


class ContinentalPage(WagtailBasePage):
    template = "home_page.jinja"
    parent_page_type = [
        'cabinsback.HomePage'
    ]
    subpage_types = [
        'cabinsback.StatePage'
    ]


class StatePage(WagtailBasePage):
    template = "home_page.jinja"
    parent_page_type = [
        'cabinsback.ContinentalPage'
    ]
    subpage_types = [
        'cabinsback.RegionalPage'
    ]


class RegionalPage(WagtailBasePage):
    template = "home_page.jinja"
    parent_page_type = [
        'cabinsback.StatePage'
    ]
    subpage_types = [
        'cabinsback.ListingPage'
    ]


class ListingPage(WagtailBasePage):
    template = "home_page.jinja"
    # Amenities
    open_dates = ClusterTaggableManager(through="cabinspage.OpenDates", blank=True, related_name="open_date")
    general = ClusterTaggableManager(through="cabinspage.General", blank=True, related_name="general")
    food_drink = ClusterTaggableManager(through="cabinspage.FoodDrink", blank=True, related_name="food_drink")
    property_size = ClusterTaggableManager(through="cabinspage.PropertySize", blank=True, related_name="property_size")
    room = ClusterTaggableManager(through="cabinspage.Room", blank=True, related_name="room")
    near_by_city = ClusterTaggableManager(through="cabinspage.NearbyCity", blank=True, related_name="near_by_city")
    activities = ClusterTaggableManager(through="cabinspage.Activities", blank=True, related_name="activities")
    near_by_water = ClusterTaggableManager(through="cabinspage.NearByWater", blank=True, related_name="near_by_water")
    services = ClusterTaggableManager(through="cabinspage.Services", blank=True, related_name="services")
    suitability = ClusterTaggableManager(through="cabinspage.Suitability", blank=True, related_name="suitability")

    # Addresses
    street = models.CharField(max_length=255)
    street2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)

    website = models.URLField()

    content_panels = WagtailBasePage.content_panels + [
        FieldPanel("website"),
        InlinePanel("listing_images", label="Listing Images")
    ]

    amenity_panels = [
        FieldPanel("open_dates", heading="Open Dates"),
        FieldPanel("general", heading="General"),
        FieldPanel("food_drink", heading="Food & Drink"),
        FieldPanel("property_size", heading="Property Size"),
        FieldPanel("near_by_city", heading="Near by Cities"),
        FieldPanel("activities", heading="Activities"),
        FieldPanel("near_by_water", heading="Near By Water"),
        FieldPanel("services", heading="Services"),
        FieldPanel("suitability", heading="Suitability"),
    ]

    address_panels = [
        FieldPanel("street", heading="Street One"),
        FieldPanel("street2", heading="Street Two"),
        FieldPanel("city", heading="City"),
        FieldPanel("region", heading="State/Region/Province"),
        FieldPanel("country", heading="Country"),
        FieldPanel("postal_code", heading="Postal Code"),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels, heading='Content'),
            ObjectList(amenity_panels, heading='Amenities'),
            ObjectList(address_panels, heading='Address'),
            ObjectList(WagtailBasePage.promote_panels, heading='SEO'),
            ObjectList(WagtailBasePage.settings_panels, heading='Settings'),
        ]
    )


class ListingImages(Orderable):
    listing_page = ParentalKey(ListingPage, related_name="listing_images", on_delete=models.CASCADE)
    image = models.ForeignKey(get_image_model_string(), on_delete=models.CASCADE)

    panels = [
        ImageChooserPanel('image')
    ]
