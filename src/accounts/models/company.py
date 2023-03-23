from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator, MaxLengthValidator, MinLengthValidator

from extensions import choices
from extensions.utils import phone_validator, email_validator


class CompanyProfile(models.Model):
    name = models.CharField(
        max_length=120,
        unique=True,
        db_index=True,
        verbose_name=_("name"),
    )
    english_name = models.CharField(
        max_length=120,
        primary_key=True,
        verbose_name=_("english name")
    )
    email = models.EmailField(
        validators=[email_validator],
        verbose_name=_("email"),
    )
    website_addr = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        verbose_name=_("website address")
    )
    # TODO: set validator
    telephone = models.CharField(
        max_length=10,
        unique=True
    )
    industry = models.ManyToManyField(
        to="Industry",
        blank=True,
        verbose_name=_("industry")
    )
    country = models.CharField(
        max_length=10,
        default="ایران",
        verbose_name=_("country")
    )
    province = models.CharField(
        max_length=105,
        verbose_name=_("province")
    )
    city = models.CharField(
        max_length=105,
        verbose_name=_("city")
    )
    logo = models.ImageField(
        upload_to="companies/logos/",
        blank=True,
        verbose_name=_("logo")
    )
    company_description = models.TextField(
        max_length=400,
        blank=True,
        verbose_name=_("company description")
    )
    company_view = models.ImageField(
        upload_to="companies/views/",
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
        choices=choices.Type_OF_OWNERSHIP,
        max_length=12,
        verbose_name=_("type of ownership")
    )
    operator = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name=_("operator")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("created at")
    )
    number_of_ad = models.PositiveIntegerField(
        default=0,
        verbose_name=_("number of advertisements")
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Company Profile")
        verbose_name_plural = _("Companies Profile")


class Industry(models.Model):
    title = models.CharField(
        max_length=120,
        verbose_name=_("title")
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Industry")
        verbose_name_plural = _("Industries")
