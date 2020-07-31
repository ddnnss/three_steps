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
            self.exclude.append('is_checked')
            self.exclude.append('is_publish')
        # if not request.user.is_superuser or not request.user.is_boss:
        #     self.exclude.append('contact_phone')
        return super(AdsAdmin, self).get_form(request, obj, **kwargs)

    def get_queryset(self, request):
        qs = super(AdsAdmin, self).get_queryset(request)
        if request.user.is_superuser or request.user.is_boss:
            return qs
        return qs.filter(created=request.user)

    inlines = [AdsImageInline]
    list_display = [
        'image_tag',
        "number",
        "name",
        "created_at",

    ]
    search_fields = ("name", "number","contact_phone")
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

