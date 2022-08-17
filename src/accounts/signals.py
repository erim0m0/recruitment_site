from .models import OtpDocument, User, Profile
from django.db.models.signals import pre_save
from django.dispatch import receiver
from extensions.utils import create_random_code



def save_active_email_code(sender, instance, *args, **kwargs):
    print(instance)
    instance.active_email_code = create_random_code()

pre_save.connect(user_pre_save, sender=User)
# todo add create profile's model signal
# todo add create OTP's model signal

