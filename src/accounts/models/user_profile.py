from django.db import models
from django.urls import reverse
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _

from extensions.utils import email_validator, national_code_validator
from extensions.choises_models import (
    PROVINCE,COUNTRIES,CITIES,
USER_GENDER, LANGUAGES

)


########## Models ##########

class MainProfile(models.Model):
    """
    Abstract Model from Other Models
    """

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        editable=False,
        null=True,
        blank=True
    )
    slug = models.SlugField(
        max_length=10,
        editable=False,
        null=True,
        blank=True,
        verbose_name=_("Slug Field")
    )

    def get_absolute_url(self):
        return reverse("profile", kwargs={"slug": self.slug})

    def __str__(self):
        return str(self.user)

    class Meta:
        abstract = True


class Profile(MainProfile):
    """
    Profile class for each user which is
    being created to hold the information
    """
    MILITARY_SERVICE_STATUS = (
        ("دارای کارت پایان خدمت", "دارای کارت پایان خدمت"),
        ("در حال خدمت", "در حال خدمت"),
        ("معاف از رزم", "معاف از رزم"),
        ("معافیت تحصیلی", "معافیت تحصیلی"),
        ("معافیت پزشکی", "معافیت پزشکی"),
        ("سایر معافیت ها", "سایر معافیت ها")
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
    # TODO: edit this field
    avatar = models.ImageField(
        null=True,
        blank=True,
        verbose_name=_("avatar")
    )
    national_code = models.CharField(
        max_length=10,
        validators=[national_code_validator],
        verbose_name=_("national_code")
    )
    passport_number = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name=_("passport_number")
    )
    country = models.CharField(
        max_length=200,
        choices=COUNTRIES,
        default="IR",
        verbose_name=_("country")
    )
    province = models.CharField(
        max_length=200,
        choices=PROVINCE,
        verbose_name=_("province")
    )
    city = models.CharField(
        max_length=200,
        choices=CITIES,
        verbose_name=_("city")
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
    date_of_birth = models.DateField(
        null=True,
        blank=True,
        verbose_name=_("Date Of Birth")
    )
    military_service_status = models.CharField(
        max_length=100,
        choices=MILITARY_SERVICE_STATUS,
        null=True,
        blank=True,
        verbose_name=_("Military Service Status")
    )
    other_exemptions = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("other_exemptions")
    )
    about_me = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("About Me")
    )

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")


class WorkExperience(MainProfile):
    """
    WorkExperience class for each user which is
    being created to hold the information
    """

    job = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("Job")
    )
    company = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        verbose_name=_("Company")
    )

    class Meta:
        verbose_name = _("Work Experience")
        verbose_name_plural = _("Work Experiences")


class EducationalRecord(MainProfile):
    """
    EducationalRecord class for each user which is
    being created to hold the information
    """

    GRADE_CHOICE = (
        ("Diploma", "دیپلم"),
        ("Associate DegreeAA", "لیسانس"),
        ("Bachelor of Science", "فوق لیسانس"),
        ("Doctor of Philosophy", "دکتری")
    )

    major = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name=_("Major")
    )
    university = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("University")
    )
    grade = models.FloatField(
        null=True,
        blank=True,
        verbose_name=_("Grade")
    )

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = _("Educational Record")
        verbose_name_plural = _("Educational Records")


class Language(MainProfile):
    name = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        choices=LANGUAGES,
        verbose_name=_("Language")
    )

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = _("Language")
        verbose_name_plural = _("Languages")


class CV(MainProfile):
    file = models.FileField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = _("CV")
        verbose_name_plural = _("Resumes")


############# Signals #############

@receiver(post_save, sender=get_user_model())
def create_profile(sender, instance, created, **kwargs):
    """
    Create another Models when a user being created ONLY
    """

    if created:
        if not instance.is_superuser:
            _models = (
                "Profile",
                "WorkExperience",
                "EducationalRecord",
                "CV"
            )
            for model in _models:
                eval(f"{model}.objects.create(user=instance, slug=instance.phone)")
