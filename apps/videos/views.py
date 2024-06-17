from typing import Any
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse

from django.core.paginator import Paginator

from apps.shared.views import BaseSharedView
from apps.users.models import User, UserProfile
from .models import Categories, Video, VideoLike
from .forms import VideoCreateForm


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

        categories = Categories.objects.all()

        if request.user.is_authenticated:
            user_profile = UserProfile.objects.get(user = request.user)
            self.context['user_profile'] = user_profile

        # get Videos in Category
        if category is not None:
            if category != "all":
                try:
                    videos = Video.objects.filter(category = Categories.objects.get(name=category)).filter(is_active=True).order_by("-created_at")
                    
                except:
                    self.context['page_obj'] = None
                    self.context['videos'] = None
                    self.context['categories'] = categories
                    return render(request, "videos/index.html", self.context)
                
            else:
                videos = Video.objects.filter(is_active=True).order_by("-created_at")
        else:
            videos = Video.objects.filter(is_active=True).order_by("-created_at")

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


class VideoCreateView(LoginRequiredMixin, BaseSharedView):
    def get(self, request):
        # html parse get
        subscriber_email = request.GET.get("email")

        # subscribers
        subscriber_email_service(request, subscriber_email, "videos:video-create")

        form = VideoCreateForm()
        if form.data:
            print(form.data)

        self.context['form'] = form

        return render(request, "videos/video-create.html", self.context)

    def post(self, request):
        form = VideoCreateForm(data=request.POST, files=request.FILES)
        # print(form.data)
        # print(request.FILES)
        if form.is_valid():
            title = form.data.get('title')
            photo = form.files.get('photo')
            video = form.files.get('video')
            description = form.data.get('description')
            content = form.data.get('content')
            category = Categories.objects.get(name = form.data.get('category'))

            video_create = Video(
                title = title,
                video = video.open("r"),
                photo = photo.open("r"),
                description = description,
                content = content,
                category = category,
                author = request.user,
                is_active = True
            )
            
            # video_create.photo.save(photo.name, photo.file., False)
            # video_create.video.save(video.name, video.read, False)
            print(video_create.photo.url)
            print(video_create.video.url)
            video_create.save()

            messages.success(request, "Successfully created video")
            return redirect(reverse("videos:video-create"))

        messages.error(request, "Error in created video field not found !")
        return redirect(reverse("videos:video-create"))


def video_like(request, video_id):
    if request.user.is_authenticated:

        # user = User.objects.get(user_id = request.user_id)
        video = Video.objects.get(video_id=video_id)

        like, created = VideoLike.objects.get_or_create(users=request.user, videos=video)
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
