from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, VideoDetailView


app_name = "videos"
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("video-detail/<str:video_id>", VideoDetailView.as_view(), name="video-detail")
]