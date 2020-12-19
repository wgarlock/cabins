from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel

from cabins.core import get_image_model_string
from cabins.page.models import AbstractBasePage


class WagtailBasePage(AbstractBasePage, Page):
    description = models.TextField()
    meta_description = models.CharField(max_length=120, blank=True, null=True)
    og_description = models.CharField(max_length=300, blank=True, null=True)
    og_image = models.ForeignKey(
        get_image_model_string(), null=True, on_delete=models.SET_NULL, related_name='+'
    )
    content_panels = Page.content_panels + [
        FieldPanel('description', classname='full'),
    ]
    promote_panels = Page.promote_panels + [
        MultiFieldPanel([
            FieldPanel('meta_description', help_text='in browser text: max chars 120'),
            FieldPanel('og_description', help_text='social media text: max chars 300'),
            ImageChooserPanel('og_image'),
        ], 'Open Graph Content'),
    ]
