from typing import Any
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse

from apps.shared.views import BaseSharedView
from apps.videos.models import Video
from .models import UserProfile, User
from .forms import UserSignUpForm, UserSignInForm, UserProfileForm

from apps.shared.services import subscriber_email_service


class UserSignUpView(BaseSharedView):
    # Registration
    def get(self, request):

        # subscribers
        subscriber_email_service(
            request,
            request.GET.get("email", None),
            "users:sign_up"
        )

        self.context["form"] = UserSignUpForm()

        return render(request, "users/sign_up.html", self.context)

    def post(self, request):
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get("username")
            password1 = form.cleaned_data.get("password1")
            password2 = form.cleaned_data.get("password2")

            if password1 == password2:
                user = authenticate(username=username, password=password2)

                if user is not None:
                    login(request, user)

                    messages.success(
                        request,
                        """You successfully registered. Welcome to VideoCatalog""",
                    )
                    return redirect("videos:home")

                else:
                    messages.error(request, "User Not Found !")
                    return redirect("users:sign_up")
            else:
                messages.error("Your Passwords are not equil.")
                return redirect("users:sign_up")

        else:
            messages.error(request, "You`r fields invalid or already token.")
            return redirect("users:sign_up")


class UserSignInView(BaseSharedView):
    # Authorization
    def get(self, request):

        # subscribers
        subscriber_email_service(
            request,
            request.GET.get("email", None),
            "users:sign_up"
        )

        form = UserSignInForm()
        self.context["form"] = form
        return render(request, "users/sign_in.html", self.context)

    def post(self, request):
        form = UserSignInForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f"You are logged in as {request.user.username}")
                return redirect("videos:home")

            else:
                messages.error(request, "Invalid username or password.")
                return redirect("users:sign_in")
        else:
            messages.error("Authorization error. You`r username or password invalid.")
            return redirect("users:sing_in")


class UserLogOutView(LoginRequiredMixin, BaseSharedView):
    # Logout
    def get(self, request):

        # subscribers
        subscriber_email_service(
            request,
            request.GET.get("email", None),
            "users:log_out"),
    
        return render(request, "users/log_out.html", self.context)

    def post(self, request):
        logout(request)
        return redirect("videos:home")


class UserProfileView(LoginRequiredMixin, BaseSharedView):
    # User Profile page
    def get(self, request, user_id):

        # subscribers
        subscriber_email_service(
            request,
            request.GET.get("email", None),
            reverse("users:profile", kwargs={"user_id": user_id}),
        )
        
        user = User.objects.get(user_id = user_id)
        user_profile = UserProfile.objects.get(user = user)
        form = UserProfileForm(instance=user)

        self.context["user_profile"] = user_profile
        self.context["form"] = form

        return render(request, "users/profile.html", self.context)

    def post(self, request, user_id):

        user = User.objects.get(user_id=user_id)
        user_profile = UserProfile.objects.get(user = user)

        form = UserProfileForm(
            data=request.POST, files=request.FILES, instance=user_profile
        )

        if form.is_valid():
            form.save()
            messages.success(request, "You successfully updated Profile")
            return redirect(reverse("users:profile", kwargs={"user_id": user_id}))

        else:
            messages.error(request, "You unsuccessfully updated your profile.")
            return redirect(reverse("users:profile", kwargs={"user_id": user_id}))


# class UserProfileUrlAdd(BaseSharedView):

#     def post(self, request, user_id):
#         form = UserUrlForm(request.POST)

#         user = UserProfile.objects.get(user = request.user)
#         url = form.data.get("url")
#         description = form.data.get("description")
        
#         UserUrls.objects.create(user = user, url = url, description = description)

#         messages.success(request, "Successfully added url in your profile")
#         return redirect(reverse("users:profile", kwargs={"user_id": user_id}))
    

class AuthorProfileView(BaseSharedView):

    def get(self, request, author_id):

        # subscribers
        subscriber_email_service(
            request,
            request.GET.get("email", None),
            reverse("users:author-profile", kwargs={"author_id": author_id})
        )

        user = User.objects.get(user_id=author_id)
        user_profile = UserProfile.objects.get(user=user)

        videos = Video.objects.filter(author=user)

        self.context["videos"] = videos
        self.context["user_profile"] = user_profile

        return render(request, "users/author-profile.html", self.context)

    def post(self, request, author_id):
        return render(request, "users/author-profile", self.context)
