from django.conf import settings

default_app_config = 'cabins.page.apps.BaseConfig'


def get_page_string():
    return getattr(settings, "CORE_PAGE_MODEL", "cabinspage.BasePage")
