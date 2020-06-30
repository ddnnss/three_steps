from django.contrib import admin
from .models import  *


class AdsImageInline(admin.TabularInline):
    model = AdsImage
    readonly_fields = ('image_tag',)
    extra = 0


class AdsAdmin(admin.ModelAdmin):
    inlines = [AdsImageInline]
    list_display = [
        'image_tag',
        "number",
        "name",
        "created_at",

    ]
    search_fields = ("name", "number")
    list_filter = (
        "category",
        "town",
        "action_type",
        "is_new_building",
        "is_checked",
        "is_publish",
        "is_hot",
        "created_at",
        "updated_at",
        'ads_type'
    )


    class Meta:
        model = Ads

admin.site.register(Metro)
admin.site.register(Category)
admin.site.register(Town)
admin.site.register(Ads,AdsAdmin)

