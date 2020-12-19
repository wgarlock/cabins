from appconf import AppConf


class CoreAppConf(AppConf):
    SITE_MODEL = "django_contrib_sites.Site"
    PAGE_MODEL = "cabinscore.BasePage"
    IMAGE_MODEL = "cabinscore.Image"

    class Meta:
        prefix = 'core'
