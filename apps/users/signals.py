from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, UserProfile


@receiver(post_save, sender=User)
def remove_from_invertory(sender, instance, created, **kwargs):
    if created:
        print(f"Creating UserProfile to User({instance})")

        UserProfile.objects.create(
            user=instance,
            first_name=instance.first_name,
            last_name=instance.last_name,
            email=instance.email
        )
    else:
        UserProfile.objects.update(
            user=instance,
            first_name=instance.first_name,
            last_name=instance.last_name,
            email=instance.email
        )
        

@receiver(post_save, sender=UserProfile)
def remove_from_invertory_user_profile(sender, instance, created, **kwargs):
    if not created:
        User.objects.update(
            first_name = instance.first_name,
            last_name = instance.last_name,
            email = instance.email
        )