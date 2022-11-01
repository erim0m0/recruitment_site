from django.db import models
from django.urls import reverse
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


########## Models ##########

class MainProfile(models.Model):
    """
    Abstract model from other models
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

    first_name = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        verbose_name=_('First Name')
    )
    last_name = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        verbose_name=_('Last Name')
    )

    email_regex = RegexValidator(
        regex="([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+",
        message=_("The email is Invalid.")
    )
    email = models.EmailField(
        null=True,
        blank=True,
        validators=[email_regex],
        verbose_name=_('Email')
    )
    avatar = models.ImageField(
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")


class PersonalInformation(MainProfile):
    """
    PersonalInformation class for each user which is
    being created to hold the information
    """

    GENDER = (
        ("Female", "F"),
        ("Male", "M")
    )
    MILITARY_SERVICE_STATUS = (
        ("end of service", "the end of service"),
        ("permanent exemption", "permanent exemption"),
        ("education pardon", "education pardon"),
        ("doing", "doing"),
        ("included", "included")
    )

    location = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name=_("Location")
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
        choices=GENDER,
        max_length=6,
        null=True,
        blank=True,
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

    class Meta:
        verbose_name = _("Personal Information")
        verbose_name_plural = _("Personal Informations")


class AboutMe(MainProfile):
    """
    AboutMe class for each user which is
    being created to hold the information
    """

    about_me = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name=_("About Me")
    )

    class Meta:
        verbose_name = _("About Me")
        verbose_name_plural = _("About Me")


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

    # employment_period = models.PositiveIntegerField()

    class Meta:
        verbose_name = _("Work Experience")
        verbose_name_plural = _("Work Experiences")


class EducationalRecord(MainProfile):
    """
    EducationalRecord class for each user which is
    being created to hold the information
    """

    GRADE_CHOICE = (
        ("diploma", "Diploma"),
        ("associate", "Associate"),
        ("master", "MA"),
        ("master of science", "MS"),
        ("doctorate", "Dr")
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
    grade = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        choices=GRADE_CHOICE,
        verbose_name=_("Grade")
    )

    class Meta:
        verbose_name = _("Educational Record")
        verbose_name_plural = _("Educational Records")


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
                "PersonalInformation",
                "AboutMe",
                "WorkExperience",
                "EducationalRecord"
            )
            for model in _models:
                eval(f"{model}.objects.create(user=instance, slug=instance.phone)")
