from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from django.db.models.signals import pre_save
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

from accounts.managers import UserManager
from extensions.utils import (
    phone_validation,
    create_random_code,
    persian_date_convertor
)


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
    phone = models.CharField(
        max_length=10,
        validators=[phone_validation],
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
    """
    Create active email code for post creating a user which activates
    """

    if kwargs.get("signal"):
        instance.active_email_code = create_random_code()
