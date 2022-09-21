from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from django.db.models.signals import pre_save
from django.core.validators import RegexValidator
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _

from extensions.utils import create_random_code
from extensions.utils import persian_date_convertor



############# Manager #############

class UserManager(BaseUserManager):

    def create_user(self, phone, password, **extra_fields):
        if not phone:
            raise ValueError(_("user must have phone"))

        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active_email", True)
        extra_fields.setdefault("user_level", "super_user")

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_admin=True."))

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self.create_user(phone, password, **extra_fields)



############# User Model #############

class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User Model for authentication management
    through email address instead of username
    """

    USER_LEVEL = (
        ("normal", "normal"),
        ("admin", "admin"),
        ("super_user", "super_user")
    )

    phone_regex = RegexValidator(
        regex="^9\d{2}\s*?\d{3}\s*?\d{4}$",
        message=_("The phone number is Invalid.")
    )
    phone = models.CharField(
        max_length=10,
        validators=[phone_regex],
        unique=True,
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

    active_email_code = models.CharField(
        max_length=32,
        editable=False,
        null=True,
        blank=True
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("date_joined")
    )

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def persian_date_created(self):
        return persian_date_convertor(self.date_joined)

    persian_date_created.short_description = "Date Joined"

    class Meta:
        ordering = ("-id",)
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.phone



############# Signals #############

@receiver(pre_save, sender=User)
def save_active_email_code(sender, instance, **kwargs):
    if kwargs.get("signal"):
        instance.active_email_code = create_random_code()
