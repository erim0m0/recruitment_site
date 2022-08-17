import datetime
import random
import string
from datetime import timedelta
from django.utils import timezone
from django.db import models
from .managers import UserManager
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from django.core.validators import (
    RegexValidator, MaxValueValidator,
    MinValueValidator
)
from django.utils.translation import gettext_lazy as _
from extensions.utils import persian_date_convertor


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User Model for authentication management through email address instead of username
    """

    phone_regex = RegexValidator(
        regex="^989\d{2}\s*?\d{3}\s*?\d{4}$",
        message=_("Invalid phone number.")
    )
    phone = models.CharField(
        max_length=12, validators=[phone_regex],
        unique=True, verbose_name=_("phone")
    )
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active_email = models.BooleanField(default=False)
    active_email_code = models.CharField(
        max_length=72, editable=False,
        null=True, blank=True
    )
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name=_("date_joined"))

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        ordering = ('-id',)
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.phone

    @property
    def is_staff(self):
        return self.is_admin

    def persian_date_created(self):
        return persian_date_convertor(self.date_joined)

    persian_date_created.short_description = "Date Joined"


class Profile(models.Model):
    """
    Profile class for each user which is being created to hold the information
    """
    pass


class OTPDocument(models.Model):
    """
        OTPDocument class for each user which is being created to hold the information
    """

    code = models.PositiveIntegerField(
        validators=[MaxValueValidator(999999), MinValueValidator(111111)],
        verbose_name=_("Otp Code")
    )
    contact = models.CharField(
        max_length=12, verbose_name=_("Contact")
    )
    create_at = models.DateTimeField(
        default=timezone.now,
        verbose_name=_("Create_at")
    )
    retry = models.IntegerField(
        default=0, verbose_name=_("Retry")
    )

    class Meta:
        verbose_name = 'Otp Service'
        verbose_name_plural = 'Otp Services'

    def __str__(self):
        return str(self.code)
