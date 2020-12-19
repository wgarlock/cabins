from django.core.cache import cache
from django.db import models

from cabins.core import get_app_site_string, get_image_model_string
from cabins.core.models import SeriailizerMixin


class AbstractBasePage(SeriailizerMixin):
    def context_builder(self, request):
        context = dict(get_app_site_string())
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
        context.update(self.context_builder(self.request))
        return context


class BasePage(AbstractBasePage, models.Model):
    description = models.TextField()
    meta_description = models.CharField(max_length=120, blank=True, null=True)
    og_description = models.CharField(max_length=300, blank=True, null=True)
    og_image = models.ForeignKey(
        get_image_model_string(), null=True, on_delete=models.SET_NULL, related_name='+'
    )
