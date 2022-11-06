from django.db import models
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
from django.core.validators import (
    RegexValidator,
    MaxLengthValidator,
    MinLengthValidator
)
from django.contrib.auth import get_user_model

from extensions.utils import phone_validator, email_validator


class Industry(models.Model):
    """
    This model is related to every organization
    in what kind of industry it is engaged in
    """
    type = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name=_("type of company")
    )

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = _("Industry")
        verbose_name_plural = _("Industries")


class CompanyProfile(models.Model):
    Type_OF_OWNERSHIP = (
        ("Private", "Private"),
        ("Government", "Government"),
        ("Other", "Non-profit/Charity")
    )

    email = models.EmailField(
        null=True,
        blank=True,
        validators=[email_validator],
        verbose_name=_("email"),
    )
    name = models.CharField(
        max_length=120,
        unique=True,
        verbose_name=_("name"),
    )
    english_name = models.CharField(
        max_length=120,
        null=True,
        blank=True,
        verbose_name=_("english name")
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
    industry = models.ForeignKey(
        Industry,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("industry")
    )
    city = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("city")
    )
    # TODO: set address of upload
    logo = models.ImageField(
        upload_to="",
        null=True,
        blank=True,
        verbose_name=_("logo")
    )
    company_description = models.TextField(
        max_length=400,
        null=True,
        blank=True,
        verbose_name=_("company description")
    )
    # TODO: set address of upload
    company_view = models.ImageField(
        upload_to="",
        null=True,
        blank=True,
        verbose_name=_("company view")
    )
    YEAR_VALIDAITOR = RegexValidator(
        regex="^13\d{2}",
        message="The year is Invalid."
    )
    established_year = models.PositiveIntegerField(
        validators=[YEAR_VALIDAITOR],
        null=True,
        blank=True,
        verbose_name=_("established year")
    )
    type_of_ownership = models.CharField(
        choices=Type_OF_OWNERSHIP,
        max_length=10,
        null=True,
        blank=True,
        verbose_name=_("type of ownership")
    )
    organizational_interface = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name=_("organizational interface")
    )
    create_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("create at")
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