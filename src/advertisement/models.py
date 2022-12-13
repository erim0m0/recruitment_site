from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator

from accounts.models.company import CompanyProfile
from extensions.choises_models import (
    GENDER,
    TYPE_OF_COOPERATION,
)
from accounts.models.user_profile import Language
from extensions.choises_models import (
    PROVINCE, COUNTRIES, MILITARY_SERVICES_STATUS,
    LANGUAGES, LANGUAGES_LEVEL, BENEFITS,
    SALARY
)


class Advertisement(models.Model):
    title = models.CharField(
        max_length=150,
        db_index=True,
        verbose_name=_("title")
    )
    organizational_category = models.CharField(
        max_length=75,
        verbose_name=_("organizational category")
    )
    type_of_cooperation = models.CharField(
        max_length=75,
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
        max_length=100,
        default="IR",
        choices=COUNTRIES,
        verbose_name=_("country")
    )
    province = models.CharField(
        max_length=200,
        choices=PROVINCE,
        verbose_name=_("province")
    )
    city = models.CharField(
        max_length=150,
        verbose_name=_("city")
    )
    is_company_have_living_place = models.BooleanField(
        default=False,
        verbose_name=_("is company have living place")
    )
    minimum_age = models.PositiveIntegerField(
        validators=[MinValueValidator(18)],
        null=True,
        blank=True,
        verbose_name=_("minimum age")
    )
    maximum_age = models.PositiveIntegerField(
        validators=[MaxValueValidator(50)],
        null=True,
        blank=True,
        verbose_name=_("maximum age")
    )
    gender = models.CharField(
        max_length=17,
        choices=GENDER,
        verbose_name=_("gender")
    )
    military_service_status = models.CharField(
        max_length=100,
        choices=MILITARY_SERVICES_STATUS,
        verbose_name=_("Military Service Status")
    )
    work_experience = models.PositiveIntegerField(
        validators=[MinValueValidator(2)],
        verbose_name=_("amount of work experience")
    )
    # TODO: edit this field
    language = models.CharField(
        max_length=100,
        choices=LANGUAGES,
        verbose_name=_("languages")
    )
    language_level = models.CharField(
        max_length=20,
        choices=LANGUAGES_LEVEL,
        verbose_name=_("language level")
    )
    # TODO: edit this field
    benefits = models.CharField(
        max_length=200,
        choices=BENEFITS,
        null=True,
        blank=True,
        verbose_name=_("benefits")
    )
    # TODO: edit this field
    salary = models.CharField(
        max_length=75,
        choices=SALARY,
        db_index=True,
        verbose_name=_("salary")
    )
    job_description = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("job description")
    )
    company = models.ForeignKey(
        CompanyProfile,
        on_delete=models.CASCADE,
        related_name="advertisements",
        editable=False
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Advertisement")
        verbose_name_plural = _("Advertisements")
