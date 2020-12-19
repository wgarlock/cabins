from django.conf import settings
from django.db import models
from django.utils.functional import cached_property
from rest_framework import serializers

from cabins.core import get_image_model_string
from cabins.core.cache import get_cached_class


class Orderable(models.Model):
    sort_order = models.IntegerField(null=True, blank=True, editable=False)
    sort_order_field = 'sort_order'

    class Meta:
        abstract = True
        ordering = ['sort_order']


class Image(models.Model):
    name = models.CharField(max_length=255)
    file = models.ImageField()


class SeriailizerMixin:
    @cached_property
    def serializer_model(self, exclude_tup=()):
        class SelfSerializer(serializers.ModelSerializer):
            def build_relational_field(self, field_name, relation_info):
                field_class, field_kwargs = super().build_relational_field(field_name, relation_info)
                if relation_info.related_model._meta.label == get_image_model_string():
                    class ImageField(serializers.RelatedField):
                        def to_representation(self, value):
                            return get_cached_class(settings.CORE_IMAGE_RENDITION).representation(value)

                    field_class = ImageField

                return field_class, field_kwargs

            class Meta:
                model = self.__class__
                exclude = exclude_tup

        return SelfSerializer

    def serialize(self):
        return self.serializer_model(self).data

    def serialize_all(self):
        return self.serializer_model()(self, many=True).data
