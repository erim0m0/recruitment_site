from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from accounts.models import User, OTPDocument


class CustomAdmin(BaseUserAdmin):
    model = User
    list_display = (
        'phone', 'is_admin', 'is_superuser',
        'is_active_email', 'persian_date_created'
    )
    list_filter = ('is_admin', 'is_superuser')
    readonly_fields = ('last_login', 'password', 'persian_date_created')
    search_fields = ('phone',)
    ordering = ('-id',)

    add_fieldsets = (
        (None, {'fields': ('phone', 'password1', 'password2')}),
    )

    fieldsets = (
        ('Authentication',
         {'fields': ('phone', 'password'), 'classes': ('collapse',)}),
        ('Permissions',
         {'fields': ('is_active', 'is_admin', 'is_superuser', 'is_active_email')}),
        ("Group Permissions",
         {'fields': ('groups', 'user_permissions')}),
        ('Important Date',
         {'fields': ('persian_date_created', 'last_login',)}),
    )

    filter_horizontal = ('groups', 'user_permissions')


@admin.register(OTPDocument)
class OtpServicesAdmin(admin.ModelAdmin):
    list_display = ('code', 'contact', 'create_at')
    readonly_fields = ('create_at',)


admin.site.register(User, CustomAdmin)
