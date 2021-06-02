from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter
from html_render_utils.html_render import HtmlRender

from supplier_models.models import Supplier


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_date', 'updated_date', 'active')
    list_display_links = ['name', ]
    list_per_page = 25
    list_filter = (
        # for ordinary fields
        ('name', DropdownFilter),
        ('is_active', DropdownFilter),
        # for choice fields
        # ('a_choicefield', ChoiceDropdownFilter),
        # for related fields
        # ('staff', RelatedDropdownFilter),
    )

    def active(self, obj):
        check = 'active' if obj.is_active else 'inactive'
        color = 'green' if obj.is_active else 'orange'
        return HtmlRender.p(text=check, color=color)


admin.site.register(Supplier, SupplierAdmin)
