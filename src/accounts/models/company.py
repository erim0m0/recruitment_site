from django.db import models
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
from django.core.validators import (
    RegexValidator, MaxLengthValidator, MinLengthValidator
)
from django.contrib.auth import get_user_model

from extensions.utils import phone_validator, email_validator, url_validator
from extensions.choises_models import (
    Type_OF_OWNERSHIP, COUNTRIES, PROVINCE, CITIES
)


class CompanyProfile(models.Model):
    name = models.CharField(
        max_length=120,
        unique=True,
        db_index=True,
        verbose_name=_("name"),
    )
    english_name = models.CharField(
        max_length=120,
        unique=True,
        null=True,
        blank=True,
        verbose_name=_("english name")
    )
    email = models.EmailField(
        validators=[email_validator],
        verbose_name=_("email"),
    )
    website_addr = models.CharField(
        max_length=120,
        null=True,
        blank=True,
        verbose_name=_("website address")
    )
    # TODO: set validator
    telephone = models.CharField(
        max_length=10,
        unique=True
    )
    industry = models.JSONField(
        default=dict,
        blank=True,
        verbose_name=_("industry")
    )
    country = models.CharField(
        max_length=100,
        default="IR",
        choices=COUNTRIES,
        verbose_name=_("country")
    )
    province = models.CharField(
        max_length=100,
        choices=PROVINCE,
        verbose_name=_("province")
    )
    city = models.CharField(
        max_length=100,
        choices=CITIES,
        verbose_name=_("city")
    )
    logo = models.URLField(
        max_length=200,
        blank=True,
        validators=[url_validator],
        verbose_name=_("logo")
    )
    company_description = models.TextField(
        max_length=400,
        null=True,
        blank=True,
        verbose_name=_("company description")
    )
    company_view = models.URLField(
        max_length=200,
        validators=[url_validator],
        blank=True,
        verbose_name=_("company view")
    )
    YEAR_VALIDAITOR = RegexValidator(
        regex="^1[34]\d{2}$",
        message="The year is Invalid."
    )
    established_year = models.PositiveIntegerField(
        validators=[YEAR_VALIDAITOR],
        verbose_name=_("established year")
    )
    type_of_ownership = models.CharField(
        choices=Type_OF_OWNERSHIP,
        max_length=12,
        verbose_name=_("type of ownership")
    )
    organizational_interface = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name=_("organizational interface")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("created at")
    )
    number_of_advertisements = models.PositiveIntegerField(
        default=0,
        verbose_name=_("number of advertisements")
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Company Profile")
        verbose_name_plural = _("Companies Profile")
