from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from django.db.models.signals import pre_save
from django.dispatch import receiver
from extensions.utils import create_random_active_email
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from extensions.utils import persian_date_convertor
from django.contrib.auth.models import BaseUserManager


# # #
# Manager
# # #

class UserManager(BaseUserManager):

    def create_user(self, phone, password, **extra_fields):
        if not phone:
            raise ValueError(_('user must have phone'))

        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password, **extra_fields):
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active_email", True)

        if extra_fields.get("is_admin") is not True:
            raise ValueError(_("Superuser must have is_admin=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(phone, password, **extra_fields)


# # #
# User Model
# # #

class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User Model for authentication management
    through email address instead of username
    """

    phone_regex = RegexValidator(
        regex="^9\d{2}\s*?\d{3}\s*?\d{4}$",
        message=_("شماره ی تلفن نامعتبر است.")
    )
    phone = models.CharField(
        max_length=12, validators=[phone_regex],
        unique=True, verbose_name=_("phone")
    )

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active_email = models.BooleanField(default=False)
    is_active_email = models.BooleanField(default=False)

    active_email_code = models.CharField(
        max_length=72, editable=False,
        null=True, blank=True
    )
    date_joined = models.DateTimeField(
        auto_now_add=True, verbose_name=_("date_joined")
    )

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        ordering = ('-id',)
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.phone

    @property
    def is_staff(self):
        return self.is_admin

    def persian_date_created(self):
        return persian_date_convertor(self.date_joined)

    persian_date_created.short_description = "Date Joined"


# # #
# Signals
# # #

@receiver(pre_save, sender=User)
def save_active_email_code(sender, instance, **kwargs):
    if kwargs.get('signal'):
        instance.active_email_code = create_random_active_email()
