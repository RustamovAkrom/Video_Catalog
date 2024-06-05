from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.shared.models import AbstractBaseModel
from uuid import uuid4

class User(AbstractUser):
    user_id = models.CharField(max_length=128, default=uuid4())

    def __str__(self) -> str:
        return self.username
    

class UserProfile(AbstractBaseModel):
    user = models.OneToOneField(User, models.DO_NOTHING, related_name="user_profile")

    def __str__(self) -> str:
        return self.user.username