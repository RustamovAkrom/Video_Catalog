from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    ContactPageView,
    VideoDetailView,
    VideoCreateView,
    video_like,
    video_download,
)


app_name = "videos"
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("video-detail/<str:video_id>", VideoDetailView.as_view(), name="video-detail"),
    path("video-create/", VideoCreateView.as_view(), name="video-create"),
    path("video-like/<str:video_id>", video_like, name="video-like"),
    path("video-download/<str:video_id>", video_download, name="video-download"),
]
