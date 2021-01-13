from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

default_app_config = 'cabins.core.apps.BaseConfig'


def get_app_site_string():
    return getattr(settings, "CORE_SITE_MODEL", "sites.Site")


def get_image_model_string():
    image_string = getattr(settings, "CORE_IMAGE_MODEL", "cabinscore.Image")
    if not image_string:
        raise NotImplementedError("CORE_IMAGE_MODEL is not implemented in this project")
    return image_string


def get_model(model_string):
    from django.apps import apps
    try:
        return apps.get_model(model_string)
    except ValueError:
        raise ImproperlyConfigured(f"{model_string} must be of the form 'app_label.model_name'")
    except LookupError:
        raise ImproperlyConfigured(
            f"{model_string} refers to model that has not been installed"
        )
