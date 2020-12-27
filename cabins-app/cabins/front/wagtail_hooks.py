from cabins.front.models import SiteContent
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register


class SiteContentAdmin(ModelAdmin):
    model = SiteContent
    menu_label = 'Site Content'
    menu_icon = 'doc-empty'
    menu_order = 200
    add_to_settings_menu = True
    exclude_from_explorer = False


modeladmin_register(SiteContentAdmin)
