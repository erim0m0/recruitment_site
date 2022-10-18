from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator


class JobIntroduction(models.Model):
    ORGANIZATIONAL_CATEGORY_CHOICES = (
        ("normal_worker", "normal_worker"),
        ("employee", "employee"),
        ("expert", "expert"),
    )
    title = models.CharField(
        max_length=150,
        verbose_name=_("title")
    )
    is_unknown = models.BooleanField(
        default=False,
        verbose_name=_("is unknown")
    )
    # TODO: Edit this field
    organizational_category = models.CharField(
        max_length=75,
        # choices=
        verbose_name=_("organizational category")
    )
    # TODO: Edit this field
    type_of_cooperation = models.CharField(
        max_length=75,
        # choices=
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


class EmploymentConditions(models.Model):
    minimum_age = models.PositiveIntegerField(
        validators=[MinValueValidator(18)],
        verbose_name=_("minimum age")
    )
    maximum_age = models.PositiveIntegerField(
        validators=[MaxValueValidator(50)],
        verbose_name=_("maximum age")
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
        verbose_name=_("amount of work experience")
    )
    languages = models.CharField(
        # choices=
        max_length=75,
        verbose_name=_("languages")
    )
