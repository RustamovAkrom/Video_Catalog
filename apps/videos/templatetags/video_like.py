from django import template
from apps.videos.models import VideoLike, Video
from apps.users.models import UserProfile

register = template.Library()


def check_like(video, user):
    print(video, user)
    user = UserProfile.objects.get(user=user)
    video_likes = VideoLike.objects.filter(users=user, videos=video)
    return video_likes.exists()


register.filter(check_like)
