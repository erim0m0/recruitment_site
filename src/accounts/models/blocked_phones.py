from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


class BlockedPhone(models.Model):
    phone_regex = RegexValidator(
        regex="^9\d{2}\s*?\d{3}\s*?\d{4}$",
        message=_("شماره ی تلفن نامعتبر است.")
    )
    phone = models.CharField(
        max_length=12,
        validators=[phone_regex],
        unique=True,
        verbose_name=_("phone")
    )

    class Meta:
        verbose_name = _("Blocked Phone")
        verbose_name_plural = _("Blocked Phones")

    def __str__(self):
        return self.phone
