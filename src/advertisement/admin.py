from django.contrib import admin
from .models import Advertisement

# Register your models here.


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ("title", "company")
