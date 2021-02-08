from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    when a user is saved, then a post_save signal is fired
    the signal is then received by the receiver

    :params sender: the user
    :params instance: instance of the user
    :params created: created user
    :params **kwargs: accepts any additional keyword arguments

    """
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    saves the profile when the user is created

    :params sender: the user
    :params instance: instance of the user
    :params **kwargs: accepts any additional keyword arguments
    """
    instance.profile.save()