from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, RegexValidator

from extensions.utils import email_validator, national_code_validator, url_validator
from extensions.choises_models import (
    PROVINCE, COUNTRIES, CITIES, USER_GENDER, P_MILITARY_SERVICE_STATUS
)


class Profile(models.Model):
    """
    Profile class for each user which is
    being created to hold the information
    """
    user = models.OneToOneField(
        get_user_model(),
        editable=False,
        on_delete=models.CASCADE,
        verbose_name=_("User")
    )
    slug = models.SlugField(
        max_length=10,
        editable=False,
        verbose_name=_("Slug Field")
    )
    first_name = models.CharField(
        max_length=150,
        verbose_name=_('First Name')
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name=_('Last Name')
    )
    email = models.EmailField(
        null=True,
        blank=True,
        validators=[email_validator],
        verbose_name=_('Email')
    )
    avatar = models.ImageField(
        upload_to="avatars/",
        null=True, blank=True,
        verbose_name=_("Avatar")
    )
    national_code = models.CharField(
        max_length=10,
        validators=[national_code_validator],
        verbose_name=_("National_code")
    )
    passport_number = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name=_("Passport_number")
    )
    country = models.CharField(
        max_length=200,
        choices=COUNTRIES,
        default="IR",
        verbose_name=_("Country")
    )
    province = models.CharField(
        max_length=200,
        choices=PROVINCE,
        verbose_name=_("Province")
    )
    city = models.CharField(
        max_length=200,
        choices=CITIES,
        verbose_name=_("City")
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
        choices=USER_GENDER,
        max_length=6,
        verbose_name=_("Gender")
    )
    day_of_birth = models.PositiveIntegerField(
        validators=[MaxValueValidator(31)],
        verbose_name=_("day of birth")
    )
    month_of_birth = models.PositiveIntegerField(
        validators=[MaxValueValidator(12)],
        verbose_name=_("month of birth")
    )
    YEAR_VALIDAITOR = RegexValidator(
        regex="^1[34]\d{2}$",
        message="The year is Invalid."
    )
    year_of_birth = models.PositiveIntegerField(
        validators=[YEAR_VALIDAITOR],
        verbose_name=_("year of birth")
    )
    # date_of_birth = models.DateField(
    #     null=True,
    #     blank=True,
    #     verbose_name=_("Date Of Birth")
    # )
    military_service_status = models.CharField(
        max_length=100,
        choices=P_MILITARY_SERVICE_STATUS,
        null=True,
        blank=True,
        verbose_name=_("Military Service Status")
    )
    other_exemptions = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("other exemptions")
    )
    about_me = models.TextField(
        max_length=400,
        null=True,
        blank=True,
        verbose_name=_("About Me")
    )
    cv_file = models.URLField(
        max_length=200,
        validators=[url_validator],
        blank=True,
        verbose_name=_("CV File")
    )
    work_experience = models.JSONField(
        default=dict,
        blank=True
    )
    educational_record = models.JSONField(
        default=dict,
        blank=True
    )
    language = models.JSONField(
        default=dict,
        blank=True
    )

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

# class WorkExperience(MainProfile):
#     """
#     WorkExperience class for each user which is
#     being created to hold the information
#     """
#
#     job = models.CharField(
#         max_length=100,
#         verbose_name=_("Job")
#     )
#     company = models.CharField(
#         max_length=150,
#         verbose_name=_("Company")
#     )
#
#     class Meta:
#         verbose_name = _("Work Experience")
#         verbose_name_plural = _("Work Experiences")


# class EducationalRecord(MainProfile):
#     """
#     EducationalRecord class for each user which is
#     being created to hold the information
#     """
#
#     major = models.CharField(
#         max_length=30,
#         verbose_name=_("Major")
#     )
#     university = models.CharField(
#         max_length=100,
#         verbose_name=_("University")
#     )
#     grade = models.FloatField(
#         default=0,
#         verbose_name=_("Grade")
#     )
#
#     class Meta:
#         verbose_name = _("Educational Record")
#         verbose_name_plural = _("Educational Records")


# class Language(MainProfile):
#     name = models.CharField(
#         max_length=200,
#         choices=LANGUAGES,
#         verbose_name=_("Language")
#     )
#
#     class Meta:
#         verbose_name = _("Language")
#         verbose_name_plural = _("")
