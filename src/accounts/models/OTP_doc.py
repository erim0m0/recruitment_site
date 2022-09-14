from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class OTPDocument(models.Model):
    """
    OTPDocument class for each user which
    wants to be create user
    """

    id_code = models.CharField(
        max_length=32,
        verbose_name=_("ID Code")
    )
    code = models.PositiveIntegerField(
        verbose_name=_("Otp Code")
    )
    contact = models.CharField(
        max_length=11,
        unique=True,
        verbose_name=_("Contact")
    )
    create_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Create_at")
    )
    retry = models.IntegerField(
        default=0,
        verbose_name=_("Retry")
    )

    class Meta:
        verbose_name = _("Otp Service")
        verbose_name_plural = _("Otp Services")

    def __str__(self):
        return str(self.code)
