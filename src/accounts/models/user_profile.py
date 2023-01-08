from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, RegexValidator

from multiselectfield import MultiSelectField

from extensions.choises_models import (
    PROVINCE, COUNTRIES, CITIES, USER_GENDER,
    P_MILITARY_SERVICE_STATUS, LANGUAGES, EDUCATION
)
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
    slug = models.SlugField(
        max_length=10,
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
    passport_number = models.CharField(
        max_length=20,
        blank=True,
        verbose_name=_("Passport number")
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
    military_service_status = models.CharField(
        max_length=100,
        choices=P_MILITARY_SERVICE_STATUS,
        verbose_name=_("Military Service Status")
    )
    other_exemptions = models.CharField(
        max_length=100,
        blank=True,
        verbose_name=_("other exemptions")
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
    language = MultiSelectField(
        choices=LANGUAGES,
        max_choices=3,
        max_length=30,
        blank=True,
        verbose_name=_("language")
    )

    def __str__(self):
        return self.user.phone

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")


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

    class Meta:
        verbose_name = _("Work Experience")
        verbose_name_plural = _("Work Experiences")


@receiver(pre_save, sender=WorkExperience)
def delete_work_exps_exist(sender, instance, **kwargs):
    WorkExperience.objects.filter(user__phone=instance.user, job=instance.job).delete()


class EducationalRecord(models.Model):
    field_of_study = models.CharField(
        max_length=30,
        verbose_name=_("field of study")
    )
    education = models.CharField(
        choices=EDUCATION,
        max_length=9,
        verbose_name=_("education")
    )
    university = models.CharField(
        max_length=100,
        verbose_name=_("University")
    )
    score = models.FloatField(
        default=0,
        validators=[MaxValueValidator(20)],
        verbose_name=_("score")
    )

    class Meta:
        verbose_name = _("Educational Record")
        verbose_name_plural = _("Educational Records")


@receiver(pre_save, sender=EducationalRecord)
def delete_work_exps_exist(sender, instance, **kwargs):
    WorkExperience.objects.filter(
        user__phone=instance.user,
        education=instance.eeducation,
        university=instance.university
    ).delete()
