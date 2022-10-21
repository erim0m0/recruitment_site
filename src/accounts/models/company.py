from django.db import models
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.utils.translation import gettext_lazy as _
from django.core.validators import (
    RegexValidator,
    MaxLengthValidator,
    MinLengthValidator
)

from extensions.utils import phone_validation


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
        verbose_name=_("email"),
    )
    # TODO: Remove a null and blank attrs
    name = models.CharField(
        max_length=120,
        null=True,
        blank=True,
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
        max_length=10
    )
    industry = models.ManyToManyField(
        Industry,
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
    established_year = models.PositiveIntegerField(
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
    # TODO : Remove null and blak fiels
    organizational_interface = models.OneToOneField(
        "OrganizationalInterface",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("organizational interface")
    )
    create_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("create at")
    )

    def __str__(self):
        if self.english_name:
            return f"{self.name}/{self.english_name}"
        return self.name

    def get_absolute_url(self):
        return reverse("account:api:company-profile", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = _("Company Profile")
        verbose_name_plural = _("Companies Profile")


class OrganizationalInterface(models.Model):
    first_name = models.CharField(
        max_length=75,
        null=True,
        blank=True,
        verbose_name=_("first name")
    )
    last_name = models.CharField(
        max_length=75,
        null=True,
        blank=True,
        verbose_name=_("last name")
    )
    organization_level = models.CharField(
        max_length=75,
        null=True,
        blank=True,
        verbose_name=_("organization level")
    )
    phone = models.CharField(
        max_length=10,
        unique=True,
        validators=[phone_validation],
        verbose_name=_("phone")
    )
    password = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name=_("password")
    )
    slug = models.SlugField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name=_("slug")
    )

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return f"{self.phone}: doesn't complete"

    def get_absolute_url(self):
        return reverse("account:api:operator-register", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = _("Organizational Interface")
        verbose_name_plural = _("Organizational Interfaces")


############# Signals #############

@receiver(pre_save, sender=OrganizationalInterface)
def save_slug_field(sender, instance, **kwargs):
    """
    Create slug field for post creating a operator's company
    """

    if kwargs.get("signal"):
        instance.slug = instance.phone
