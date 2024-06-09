from django.contrib import admin
from .models import Categories, Video, VideoLike, SubscribersEmail


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    pass


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass


@admin.register(VideoLike)
class VideoLikesAdmin(admin.ModelAdmin):
    pass


@admin.register(SubscribersEmail)
class SubscribersEmailAdmin(admin.ModelAdmin):
    pass
