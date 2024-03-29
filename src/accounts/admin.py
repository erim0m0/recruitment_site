from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from accounts.models import users, blocked_phones, user_profile, company


class CustomAdmin(BaseUserAdmin):
    model = users.User
    list_display = (
        'phone', 'user_level', 'is_operator',
        'is_active_email', 'persian_date_created'
    )
    list_filter = ('is_superuser',)
    readonly_fields = ('last_login', 'password',
                       'persian_date_created',
                       'active_email_code')
    search_fields = ('phone',)
    ordering = ('phone',)

    add_fieldsets = (
        (None, {'fields': ('phone', 'password1', 'password2')}),
    )

    fieldsets = (
        ('Authentication',
         {'fields': ('phone', 'password', 'active_email_code'),
          'classes': ('collapse',)}),
        ('Permissions',
         {'fields': ('user_level', 'is_active_email', 'is_operator')}),
        ("Group Permissions",
         {'fields': ('groups', 'user_permissions')}),
        ('Important Date',
         {'fields': ('persian_date_created', 'last_login',)}),
    )

    filter_horizontal = ('groups', 'user_permissions')


@admin.register(blocked_phones.BlockedPhone)
class BlockPhonesAdmin(admin.ModelAdmin):
    list_display = ('phone',)


@admin.register(company.CompanyProfile)
class BlockPhonesAdmin(admin.ModelAdmin):
    list_display = (
        "name", "operator",
        "number_of_ad"
    )


@admin.register(company.Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = (
        "title",
    )

@admin.register(company.IndustryChild)
class IndustryChildAdmin(admin.ModelAdmin):
    list_display = (
        "title",
    )


admin.site.register(users.User, CustomAdmin)
admin.site.register(user_profile.Profile)
admin.site.register(user_profile.WorkExperience)
admin.site.register(user_profile.EducationalRecord)
admin.site.register(user_profile.Language)
