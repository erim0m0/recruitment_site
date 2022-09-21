from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    """
    Profile class for each user which is
    being created to hold the information
    """

    first_name = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        verbose_name=_('Last Name')
    )
    last_name = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        verbose_name=_('First Name')
    )

    email_regex = RegexValidator(
        regex="([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+",
        message=_("The email is Invalid.")
    )
    email = models.EmailField(
        null=True,
        blank=True,
        validators=[email_regex],
        verbose_name=_('Email')
    )
    avatar = models.ImageField(
        null=True,
        blank=True
    )

    # personal_information =
    # about_me =
    # educational_records =
    # work_experience =
    # languages =
    # cv =

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class PersonalInformation(models.Model):
    GENDER = (
        ("F", "Female"),
        ("M", "Male")
    )

    MILITARY_SERVICE_STATUS = (
        ("end of service", "the end of service"),
        ("permanent exemption", "permanent exemption"),
        ("education pardon", "education pardon"),
        ("doing", "doing"),
        ("included", "included")
    )

    location = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name=_("Location")
    )

    address = models.TextField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name=_("Address")
    )
    is_married = models.BooleanField(
        default=False,
        verbose_name=_("Is Married ?")
    )

    gender = models.CharField(
        choices=GENDER,
        max_length=6,
        null=True,
        blank=True,
        verbose_name=_("Gender")
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
        verbose_name=_("Date Of Birth")
    )
    military_service_status = models.CharField(
        max_length=100,
        choices=MILITARY_SERVICE_STATUS,
        null=True,
        blank=True,
        verbose_name=_("Military Service Status")
    )
