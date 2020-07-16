from django.contrib import admin
from .models import  *


class AdsImageInline(admin.TabularInline):
    model = AdsImage
    readonly_fields = ('image_tag',)
    extra = 0

class SubcatInline(admin.TabularInline):
    model = SubCategory
    extra = 0


class CatAdmin(admin.ModelAdmin):
    inlines = [SubcatInline]
    extra = 0

class AdsAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if request.user.is_test:
            self.exclude.append('is_checked')  # here!
            self.exclude.append('is_publish')  # here!
        return super(AdsAdmin, self).get_form(request, obj, **kwargs)
    inlines = [AdsImageInline]
    list_display = [
        'image_tag',
        "number",
        "name",
        "created_at",

    ]
    search_fields = ("name", "number")
    list_filter = (
        "is_checked",
        "is_publish",
        'ads_type',
        "category",
        "subcategory",
        "town",
        "action_type",
        "is_new_building",
        "is_hot",
        "created_at",
        "updated_at",
    )


    class Meta:
        model = Ads

admin.site.register(Metro)
admin.site.register(Category,CatAdmin)
admin.site.register(SubCategory)
admin.site.register(Town)
admin.site.register(Ads,AdsAdmin)

