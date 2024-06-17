from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.shared.models import AbstractBaseModel
from uuid import uuid4

from _config_ import settings


class User(AbstractUser):
    user_id = models.CharField(max_length=128, default=uuid4())

    def __str__(self) -> str:
        return self.username

    

class UserProfile(AbstractBaseModel):
    user = models.OneToOneField(User, models.CASCADE, related_name="user_profile")
    first_name = models.CharField(max_length=150)      
    last_name = models.CharField(max_length=150)  
    username = models.CharField(max_length=150)
    email = models.EmailField()
    bio = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.ImageField(
        upload_to="users/avatar/",
        blank=True,
        null=True,
        default=f"{settings.DEFAULT_AUTH_USER_AVATAR_DIR}/{settings.DEFAULT_AUTH_USER_AVATAR_NAME}",
    )

    def __str__(self) -> str:
        return self.user.username
