from django.contrib import admin
from .models import *

class CallbackAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "phone",
        "time",
        "is_viewed",
    ]
    search_fields = ("name","phone",)
    list_filter = (
        "is_viewed",
        "created_at",
    )
    list_display_links = ("name",)
    list_editable = ("is_viewed",)

    class Meta:
        model = Callback



admin.site.register(Vacancy)
admin.site.register(VacancyApply)
admin.site.register(Consultation)
admin.site.register(Callback,CallbackAdmin)
