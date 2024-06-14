from typing import Any
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse

from django.core.paginator import Paginator

from apps.shared.views import BaseSharedView
from apps.users.models import UserProfile
from .models import Categories, Video, VideoLike

from apps.shared.services import subscriber_email_service


class HomePageView(BaseSharedView):
    def get(self, request):

        # html parse get
        page = request.GET.get("page", 1)
        size = request.GET.get("size", 6)
        subscriber_email = request.GET.get("email", None)
        category = request.GET.get("category", None)

        # subscrivers
        subscriber_email_service(request, subscriber_email, "videos:home")

        if request.user.is_authenticated:
            user_profile = UserProfile.objects.get(user = request.user)
            self.context['user_profile'] = user_profile

        # get Videos in Category
        if category is not None:
            if category != "all":
                videos = Video.objects.filter(is_active=True).filter(
                    category=Categories.objects.get(name=category)
                ).order_by("-created_at")

            else:
                videos = Video.objects.filter(is_active=True).order_by("-created_at")
        else:
            videos = Video.objects.filter(is_active=True).order_by("-created_at")

        categories = Categories.objects.all()

        if len(videos) >= size:
            paginator = Paginator(videos, size)
            page_obj = paginator.get_page(page)
            self.context['page_obj'] = page_obj
            self.context['videos'] = page_obj

        else:
            self.context['page_obj'] = None
            self.context['videos'] = videos

        self.context["categories"] = categories
        self.context["paginator_size"] = size

        return render(request, "videos/index.html", self.context)


class AboutPageView(BaseSharedView):
    def get(self, request):

        # html parse get
        subscriber_email = request.GET.get("email")

        # subscribers
        subscriber_email_service(request, subscriber_email, "videos:about")

        return render(request, "videos/about.html", self.context)


class ContactPageView(BaseSharedView):
    def get(self, request):

        # html parse get
        subscriber_email = request.GET.get("email")

        subscriber_email_service(request, subscriber_email, "videos:contact")

        return render(request, "videos/contact.html", self.context)

    def post(self, request):
        return render(request, "videos/contact.html")


class VideoDetailView(BaseSharedView):
    def get(self, request, video_id):

        # html parse get
        subscriber_email = request.GET.get("email")

        # subscribers
        subscriber_email_service(
            request,
            subscriber_email,
            reverse("videos:video-detail", kwargs={"video_id": video_id}),
        )

  
        videos = Video.objects.filter(is_active=True)

        video = Video.objects.get(video_id=video_id)
        related_viideos = videos.filter(category=video.category)

        self.context["related_videos"] = related_viideos
        self.context["video"] = video

        return render(request, "videos/video-detail.html", self.context)


def video_like(request, video_id):
    if request.user.is_authenticated:

        user = UserProfile.objects.get(user=request.user)
        video = Video.objects.get(video_id=video_id)

        like, created = VideoLike.objects.get_or_create(users=user, videos=video)
        if not created:
            like.delete()

        return redirect(reverse("videos:video-detail", kwargs={"video_id": video_id}))

    else:
        messages.info(request, "Pleace authorizated to system...")
        return redirect("users:sign_in")


def video_download(request, video_id):

    if request.method == "POST":

        video = Video.objects.get(video_id=video_id)
        video.add_download_count()

        return redirect(reverse("videos:video-detail", kwargs={"video_id": video_id}))
