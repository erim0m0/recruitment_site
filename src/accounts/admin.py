from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from accounts.models import User


class CustomAdmin(BaseUserAdmin):
    model = User
    list_display = ('phone', 'is_active', 'is_admin', 'is_superuser')
    list_filter = ('is_active', 'is_admin', 'is_superuser')
    readonly_fields = ('last_login', 'password')
    search_fields = ('phone',)
    ordering = ('pk',)

    fieldsets = (
        ('Authentication', {'fields': ('phone', 'password'), 'classes': ('collapse',)}),
        ('Permissions', {'fields': ('is_active', 'is_admin', 'is_superuser', 'is_active_email')}),
        ("Group Permissions", {'fields': ('groups', 'user_permissions')}),
        ('Important Date', {'fields': ('last_login',)}),
    )

    filter_horizontal = ('groups', 'user_permissions')


admin.site.register(User, CustomAdmin)
