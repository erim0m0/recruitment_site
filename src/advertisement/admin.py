from django.contrib import admin
from .models import Advertisement, FacilitiesAndBenefits

# Register your models here.

admin.site.register(FacilitiesAndBenefits)


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ("title", "company",)
