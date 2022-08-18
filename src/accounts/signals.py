from .models import User, Profile
from django.db.models.signals import pre_save
from django.dispatch import receiver
from extensions.utils import create_random_code


@receiver(pre_save, sender=User)
def save_active_email_code(sender, instance, **kwargs):
    if kwargs.get('signal'):
        instance.active_email_code = create_random_code()

# todo add create profile's model signal
