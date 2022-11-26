from django.contrib import admin
from .models import Advertisement, FacilitiesAndBenefits, MilitaryServiceStatus

# Register your models here.

admin.site.register(FacilitiesAndBenefits)
admin.site.register(MilitaryServiceStatus)


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ("title", "company")
