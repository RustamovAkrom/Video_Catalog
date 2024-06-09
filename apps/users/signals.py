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
            username=instance.username,
            email=instance.email,
        )
