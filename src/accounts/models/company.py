from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


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
        "Industry",
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

    def __str__(self):
        if self.english_name:
            return f"{self.name}/{self.english_name}"
        return self.name

    class Meta:
        verbose_name = _("Company Profile")
        verbose_name_plural = _("Companies Profile")


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


class OrganizationalInterface(models.Model):
    first_name = models.CharField(
        max_length=75,
        verbose_name=_("first name")
    )
    last_name = models.CharField(
        max_length=75,
        verbose_name=_("last name")
    )
    organization_level = models.CharField(
        max_length=75,
        verbose_name=_("organization level")
    )
    company = models.OneToOneField(
        CompanyProfile,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("company")
    )

    phone_regex = RegexValidator(
        regex="^9\d{2}\s*?\d{3}\s*?\d{4}$",
        message=_("The phone number is Invalid.")
    )
    phone = models.CharField(
        max_length=10,
        validators=[phone_regex],
        verbose_name=_("phone")
    )

    def __str__(self):
        return f"{self.last_name} / {self.company}"

    class Meta:
        verbose_name = _("Organizational Interface")
        verbose_name_plural = _("Organizational Interfaces")
