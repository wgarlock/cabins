from django.db import models
from django.utils.functional import cached_property
from rest_framework import serializers


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
    def serializer_model(self):
        class SelfSerializer(serializers.ModelSerializer):
            class Meta:
                model = self.__class__
                fields = "__all__"

        return SelfSerializer

    def serialize(self):
        return self.serializer_model()(self).data

    def serialize_all(self):
        return self.serializer_model()(self, many=True).data
