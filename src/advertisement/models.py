from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator

from extensions import choices
from accounts.models.user_profile import Language
from accounts.models.company import CompanyProfile


class Advertisement(models.Model):
    title = models.CharField(
        max_length=50,
        db_index=True,
        verbose_name=_("title")
    )
    organizational_category = models.CharField(
        max_length=40,
        verbose_name=_("organizational category")
    )
    type_of_cooperation = models.CharField(
        max_length=9,
        choices=choices.TYPE_OF_COOPERATION,
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
        max_length=20,
        default="IR",
        verbose_name=_("Country")
    )
    province = models.CharField(
        max_length=30,
        verbose_name=_("Province")
    )
    city = models.CharField(
        max_length=50,
        verbose_name=_("City")
    )
    is_company_have_living_place = models.BooleanField(
        default=False,
        verbose_name=_("Is company have living place?")
    )
    minimum_age = models.PositiveIntegerField(
        validators=[MinValueValidator(18)],
        default=18,
        blank=True,
        verbose_name=_("Minimum age")
    )
    maximum_age = models.PositiveIntegerField(
        validators=[MaxValueValidator(50)],
        default=50,
        blank=True,
        verbose_name=_("Maximum age")
    )
    gender = models.CharField(
        max_length=17,
        choices=choices.GENDER,
        verbose_name=_("gender")
    )
    military_service_status = models.CharField(
        max_length=34,
        choices=choices.AD_MILITARY_SERVICES_STATUS,
        verbose_name=_("Military Service Status")
    )
    work_experience = models.PositiveIntegerField(
        validators=[MinValueValidator(2)],
        default=2,
        verbose_name=_("amount of work experience")
    )
    # todo : edit this
    language = models.ManyToManyField(
        to=Language,
        blank=True,
        verbose_name=_("Languages")
    )
    # todo : edit this ( make a another model )
    language_level = models.CharField(
        max_length=5,
        blank=True,
        choices=choices.LANGUAGES_LEVEL,
        verbose_name=_("language level")
    )
    benefits = models.ManyToManyField(
        to="Benefit",
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
        max_length=500,
        blank=True,
        verbose_name=_("Job Description")
    )
    company = models.ForeignKey(
        CompanyProfile,
        on_delete=models.CASCADE,
        null=True,
        related_name="advertisements",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Advertisement")
        verbose_name_plural = _("Advertisements")


class Benefit(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name=_("title")
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Benefit")
        verbose_name_plural = _("Benefits")
