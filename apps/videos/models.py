from django.db import models
from apps.shared.models import AbstractBaseModel
from apps.users.models import UserProfile
from uuid import uuid4


class Categories(AbstractBaseModel):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Video(AbstractBaseModel):
    video_id = models.CharField(max_length=180, default=uuid4())
    title = models.CharField(max_length=80)
    photo = models.ImageField(upload_to="photos/%Y/%M/%D/")
    video = models.FileField(upload_to="videos/%Y/%M/%D/")
    author = models.ForeignKey(UserProfile, models.CASCADE, related_name="video_author")
    description = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey(
        Categories, models.CASCADE, related_name="video_categories"
    )
    is_active = models.BooleanField(default=False)
    downloads = models.IntegerField(default=0)

    def add_download_count(self):
        self.downloads += 1
        self.save()

    def video_like(self):
        return self.video_likes.count()

    def __str__(self) -> str:
        return self.title


class VideoLike(AbstractBaseModel):
    users = models.ForeignKey(
        UserProfile, models.DO_NOTHING, related_name="video_likes"
    )
    videos = models.ForeignKey(Video, models.CASCADE, related_name="video_likes")

    def __str__(self) -> str:
        return f"{self.videos} - like - {self.users}"


class SubscribersEmail(AbstractBaseModel):
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.email
