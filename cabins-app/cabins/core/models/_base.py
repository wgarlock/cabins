from django.db import models
from graphql import get_default_backend

from cabins.core.cache import get_class
from cabins.core.exceptions import SerializerError


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

    backend = get_default_backend()

    def get_schema(self):
        return get_class("cabins.api.schema:schema")

    serialize_attrs = """
        id
        title
        description
        heroImage{
            jpeg400
            jpeg800
            jpeg1960
        }
        ogImage{
            jpeg400
            jpeg800
            jpeg1960
        }
    """

    def get_query(self):
        return f"""query {{
            {self.serializer_request_string()} (id: {self.id}) {{
                {self.serialize_attrs}
            }}
        }}
        """

    def get_all_query(self):
        return f"""query {{
            {self.serializer_all_request_string()} {{
                {self.serialize_attrs}
            }}
        }}
        """

    def serializer_request_string(self):
        return f"get{self.__class__.__name__}ById"

    def serializer_all_request_string(self):
        return f"all{self.__class__.__name__}s"

    def create_document_data(self, query):
        return self.get_schema().execute(query).data

    def base_serializer(self, string, query):
        data = self.create_document_data(query)
        serialization = data.get(string)
        if serialization:
            return serialization
        else:
            raise SerializerError(f"{string} is not a valid key in the serialization dictionary")

    def serialize(self):
        return self.base_serializer(self.serializer_request_string(), self.get_query())

    def serialize_all(self):
        return self.base_serializer(self.serializer_all_request_string(), self.get_all_query())
