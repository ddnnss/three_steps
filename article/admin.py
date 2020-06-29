from django.contrib import admin
from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "is_active",
        "created_at",
    ]
    search_fields = ("name",)
    list_filter = (
        "is_active",
        "created_at",
    )
    list_display_links = ("name",)
    list_editable = ("is_active",)

    class Meta:
        model = Article


admin.site.register(Article, ArticleAdmin)
