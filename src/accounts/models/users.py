from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from accounts.managers import UserManager
from extensions.utils import phone_validator, create_random_code, persian_date_convertor


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User Model for authentication management
    through phone instead of username
    """

    USER_LEVEL = (
        ("normal", "normal"),
        ("admin", "admin"),
        ("super_user", "super_user")
    )
    phone = models.CharField(
        max_length=10,
        unique=True,
        validators=[phone_validator],
        verbose_name=_("phone")
    )
    user_level = models.CharField(
        choices=USER_LEVEL,
        max_length=10,
        default="normal",
        verbose_name=_("user level")
    )

    is_staff = models.BooleanField(default=False)
    is_active_email = models.BooleanField(default=False)
    is_operator = models.BooleanField(default=False)

    active_email_code = models.CharField(
        max_length=32,
        editable=False
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("date joined")
    )

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def persian_date_created(self):
        return persian_date_convertor(self.date_joined)

    persian_date_created.short_description = "Date Joined"

    def save(self, *args, **kwargs):
        self.active_email_code = create_random_code()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
