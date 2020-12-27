from cabins.core.cache import get_class
from django.db import models
from graphql import get_default_backend


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
    # convert TaggableManager to string representation

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
            get{self.__class__.__name__}ById (id: {self.id}) {{
                {self.serialize_attrs}
            }}
        }}
        """

    def get_all_query(self):
        return f"""query {{
            all{self.__class__.__name__}s {{
                {self.serialize_attrs}
            }}
        }}
        """

    def serialize(self):
        return self.backend.document_from_string(
            self.get_schema(),
            self.get_query()
        ).execute().data.get(
            f"get{self.__class__.__name__}ById"
        )

    def serialize_all(self):
        return self.backend.document_from_string(
            self.get_schema(),
            self.get_all_query()
        ).execute().data.get(
            f"all{self.__class__.__name__}s"
        )
