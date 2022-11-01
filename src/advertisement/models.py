from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from django.dispatch import receiver
from django.db.models.signals import pre_save

from accounts.models.company import CompanyProfile
from .choises_models import GENDER, TYPE_OF_COOPERATION, ORGANIZATIONAL_CATEGORY_CHOICES


class Advertisement(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name=_("title")
    )
    is_unknown = models.BooleanField(
        default=False,
        verbose_name=_("is unknown")
    )
    organizational_category = models.CharField(
        max_length=75,
        choices=ORGANIZATIONAL_CATEGORY_CHOICES,
        verbose_name=_("organizational category")
    )
    type_of_cooperation = models.CharField(
        max_length=75,
        choices=TYPE_OF_COOPERATION,
        verbose_name=_("type of cooperation")
    )
    country = models.CharField(
        max_length=100,
        verbose_name=_("country")
    )
    city = models.CharField(
        max_length=100,
        verbose_name=_("city")
    )
    living_same_city_preference = models.BooleanField(
        default=False,
        verbose_name=_("living same city preference")
    )
    remote = models.BooleanField(
        default=False,
        verbose_name=_("remote")
    )
    work_time = models.CharField(
        max_length=250,
        verbose_name=_("work time")
    )
    minimum_age = models.PositiveIntegerField(
        validators=[MinValueValidator(18)],
        verbose_name=_("minimum age")
    )
    maximum_age = models.PositiveIntegerField(
        validators=[MaxValueValidator(50)],
        verbose_name=_("maximum age")
    )
    gender = models.CharField(
        max_length=17,
        choices=GENDER,
        verbose_name=_("gender")
    )
    get_intern = models.BooleanField(
        default=False,
        verbose_name=_("get intern")
    )
    exemption_or_complete_military_service = models.BooleanField(
        default=False,
        verbose_name=_("exemption or complete military service")
    )
    amount_of_work_experience = models.PositiveIntegerField(
        validators=[MinValueValidator(2)],
        verbose_name=_("amount of work experience")
    )
    # TODO: edit this field
    languages = models.CharField(
        # choices=
        max_length=75,
        verbose_name=_("languages")
    )
    benefits = models.ManyToManyField(
        "FacilitiesAndBenefits",
        null=True,
        blank=True
    )
    salary = models.CharField(
        max_length=75,
        verbose_name=_("salary")
    )
    is_show_salary = models.BooleanField(
        default=False,
        verbose_name=_("show salary")
    )
    job_description = models.TextField(
        max_length=500,
        verbose_name=_("job description")
    )
    company = models.ForeignKey(
        CompanyProfile,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="advertisements"
        # editable=False
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Advertisement")
        verbose_name_plural = _("Advertisements")


class FacilitiesAndBenefits(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name=_("title")
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Facilities And Benefits")
        verbose_name_plural = _("Facilities And Benefits")

# @receiver(pre_save, sender=Advertisement)
# def save_company_field(instance, created, **kwargs):
#     if created:
#         instance.company = CompanyProfile.objects.filter()
