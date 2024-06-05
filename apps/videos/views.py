from typing import Any
from django.shortcuts import render, redirect
from apps.shared.views import BaseSharedView
from django.contrib import messages
from django.urls import reverse

from .models import Categories, Video, SubscribersEmail

    
class HomePageView(BaseSharedView):
    def get(self, request):

        subscriber_email = request.GET.get("email")
        if subscriber_email is not None:
            try:
                SubscribersEmail.objects.create(email = subscriber_email)
                messages.success(request, "You Successfully subscribed")
                return redirect("videos:home")
            except:
                messages.error(request, "You`r email already token.")
                return redirect("videos:home")
        
        videos = Video.objects.filter(is_active = True)

        self.context['videos'] = videos

        return render(request, "videos/index.html", self.context)
    

class AboutPageView(BaseSharedView):
    def get(self, request):

        subscriber_email = request.GET.get("email")
        if subscriber_email is not None:
            try:
                SubscribersEmail.objects.create(email = subscriber_email)
                messages.success(request, "You Successfully subscribed")
                return redirect("videos:about")
            except:
                messages.error(request, "You`r email already token.")
                return redirect("videos:about")
            
        return render(request, "videos/about.html", self.context)


class ContactPageView(BaseSharedView):
    def get(self, request):

        subscriber_email = request.GET.get("email")
        if subscriber_email is not None:
            try:
                SubscribersEmail.objects.create(email = subscriber_email)
                messages.success(request, "You Successfully subscribed")
                return redirect("videos:contact")
            except:
                messages.error(request, "You`r email already token.")
                return redirect("videos:contact")
            
        return render(request, "videos/contact.html", self.context)

    def post(self, request):
        return render(request, "videos/contact.html")


class VideoDetailView(BaseSharedView):
    def get(self, request, video_id):

        subscriber_email = request.GET.get("email")
        if subscriber_email is not None:
            try:
                SubscribersEmail.objects.create(email = subscriber_email)
                messages.success(request, "You Successfully subscribed")
                return redirect("videos:video-detail", kwargs={"video_id": video_id})
            except:
                messages.error(request, "You`r email already token.")
                return redirect("videos:home", kwargs={"video_id": video_id})
            
        videos = Video.objects.filter(is_active = True)
        print(video_id)
        video = videos.get(video_id = video_id)
        print(video)
        related_viideos = videos.filter(category = video.category)
        # related_videos = videos.filter(category = video.category.name)

        self.context['related_videos'] = related_viideos
        self.context['video'] = video

        return render(request, "videos/video-detail.html", self.context)

