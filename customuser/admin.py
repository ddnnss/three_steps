from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import *


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        (_('Personal info'), {'fields': ( 'phone','first_name','last_name',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser','is_moderator','is_test','is_boss',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'phone'),
        }),
    )
    list_display = ('id','email', 'first_name','last_name',  'phone')

    ordering = ('id',)
    search_fields = ('email', 'id', 'phone','first_name','last_name',)



