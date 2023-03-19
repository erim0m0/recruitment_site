from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, RegexValidator

from extensions import choices
from extensions.utils import email_validator, national_code_validator


class Profile(models.Model):
    """
    Profile class for each user which is
    being created to hold the information
    """

    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name=_("User")
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
        blank=True,
        validators=[email_validator],
        verbose_name=_('Email')
    )
    avatar = models.ImageField(
        upload_to="profiles/avatars/",
        blank=True,
        verbose_name=_("Avatar")
    )
    national_code = models.CharField(
        max_length=10,
        unique=True,
        validators=[national_code_validator],
        verbose_name=_("National code")
    )
    # todo: set validator
    passport_number = models.CharField(
        max_length=20,
        blank=True,
        verbose_name=_("Passport number")
    )
    # todo: set max_length
    country = models.CharField(
        max_length=20,
        default="ایران",
        verbose_name=_("Country")
    )
    # todo: set max_length
    province = models.CharField(
        max_length=100,
        verbose_name=_("Province")
    )
    # todo: set max_length
    city = models.CharField(
        max_length=100,
        verbose_name=_("City")
    )
    address = models.TextField(
        max_length=300,
        blank=True,
        verbose_name=_("Address")
    )
    is_married = models.BooleanField(
        default=False,
        verbose_name=_("Is Married ?")
    )
    gender = models.CharField(
        choices=choices.USER_GENDER,
        max_length=6,
        verbose_name=_("Gender")
    )
    date_of_birth = models.DateField(
        verbose_name=_("Date Of Birth")
    )
    military_service_status = models.CharField(
        max_length=100,
        choices=choices.P_MILITARY_SERVICE_STATUS,
        verbose_name=_("Military Service Status")
    )
    other_exemptions = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("Other Exemptions")
    )
    about_me = models.TextField(
        max_length=300,
        blank=True,
        verbose_name=_("About Me")
    )
    cv_file = models.ImageField(
        upload_to="profiles/resumes/",
        blank=True,
        verbose_name=_("CV File")
    )
    language = models.ManyToManyField(
        "Language",
        blank=True,
        verbose_name=_("Language")
    )

    def __str__(self):
        return self.user.phone

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")


class Language(models.Model):
    title = models.CharField(
        max_length=10,
        unique=True,
        verbose_name=_("title")
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Language")
        verbose_name_plural = _("Languages")


class WorkExperience(models.Model):
    user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        verbose_name=_("user")
    )
    job = models.CharField(
        max_length=50,
        verbose_name=_("Job")
    )
    company = models.CharField(
        max_length=100,
        verbose_name=_("Company")
    )

    def __str__(self):
        return f"{self.user} - {self.job}"


    class Meta:
        unique_together = ("user", "job")
        verbose_name = _("Work Experience")
        verbose_name_plural = _("Work Experiences")


class EducationalRecord(models.Model):
    user = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
        verbose_name=_("user")
    )
    field_of_study = models.CharField(
        max_length=30,
        verbose_name=_("field of study")
    )
    education = models.CharField(
        choices=choices.EDUCATION,
        max_length=9,
        verbose_name=_("education")
    )
    university = models.CharField(
        max_length=50,
        verbose_name=_("University")
    )
    score = models.FloatField(
        default=0,
        validators=[MaxValueValidator(20)],
        verbose_name=_("score")
    )

    def __str__(self):
        return f"{self.user} - {self.field_of_study}"

    class Meta:
        unique_together = ("user", "education")
        verbose_name = _("Educational Record")
        verbose_name_plural = _("Educational Records")
