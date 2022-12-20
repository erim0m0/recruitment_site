from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator

from accounts.models.company import CompanyProfile
from extensions.choises_models import (
    PROVINCE, COUNTRIES, AD_MILITARY_SERVICES_STATUS,
    LANGUAGES, LANGUAGES_LEVEL, BENEFITS, GENDER,
    SALARY, TYPE_OF_COOPERATION, CITIES
)


class Advertisement(models.Model):
    title = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name=_("title")
    )
    organizational_category = models.CharField(
        max_length=75,
        verbose_name=_("organizational category")
    )
    type_of_cooperation = models.CharField(
        max_length=9,
        choices=TYPE_OF_COOPERATION,
        verbose_name=_("type of cooperation")
    )
    # Todo: Edit it
    work_time = models.TimeField(
        max_length=250,
        null=True,
        blank=True,
        verbose_name=_("work time")
    )
    country = models.CharField(
        max_length=2,
        default="IR",
        choices=COUNTRIES,
        verbose_name=_("Country")
    )
    province = models.CharField(
        max_length=19,
        choices=PROVINCE,
        verbose_name=_("Province")
    )
    city = models.CharField(
        max_length=50,
        choices=CITIES,
        verbose_name=_("City")
    )
    is_company_have_living_place = models.BooleanField(
        default=False,
        verbose_name=_("Is company have living place")
    )
    minimum_age = models.PositiveIntegerField(
        validators=[MinValueValidator(18)],
        blank=True,
        verbose_name=_("Minimum age")
    )
    maximum_age = models.PositiveIntegerField(
        validators=[MaxValueValidator(50)],
        blank=True,
        verbose_name=_("Maximum age")
    )
    gender = models.CharField(
        max_length=17,
        choices=GENDER,
        verbose_name=_("gender")
    )
    military_service_status = models.CharField(
        max_length=34,
        choices=AD_MILITARY_SERVICES_STATUS,
        verbose_name=_("Military Service Status")
    )
    work_experience = models.PositiveIntegerField(
        validators=[MinValueValidator(2)],
        default=2,
        verbose_name=_("amount of work experience")
    )
    # TODO: edit this field
    language = models.CharField(
        max_length=100,
        # choices=LANGUAGES,
        verbose_name=_("Languages")
    )
    language_level = models.CharField(
        max_length=5,
        choices=LANGUAGES_LEVEL,
        verbose_name=_("language level")
    )
    # TODO: edit this field
    benefits = models.CharField(
        max_length=200,
        choices=BENEFITS,
        blank=True,
        verbose_name=_("Benefits")
    )
    # TODO: edit this field
    salary = models.CharField(
        max_length=75,
        # choices=SALARY,
        db_index=True,
        verbose_name=_("Salary")
    )
    job_description = models.TextField(
        max_length=400,
        blank=True,
        verbose_name=_("Job Description")
    )
    company = models.ForeignKey(
        CompanyProfile,
        on_delete=models.CASCADE,
        related_name="advertisements",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Advertisement")
        verbose_name_plural = _("Advertisements")
