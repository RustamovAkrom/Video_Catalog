from typing import Any
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse

from apps.shared.views import BaseSharedView
from .models import UserProfile
from .forms import UserSignUpForm, UserSignInForm, UserProfileForm


class UserSignUpView(BaseSharedView):
    # Registration
    def get(self, request):
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


class UserLogOutView(BaseSharedView):
    # Logout
    def get(self, request):
        return render(request, "users/log_out.html", self.context)

    def post(self, request):
        logout(request)
        return redirect("videos:home")


class UserProfileView(LoginRequiredMixin, BaseSharedView):
    # User Profile page
    def get(self, request, username):

        user_profile = UserProfile.objects.get(username=username)
        form = UserProfileForm(instance=user_profile)

        self.context["user_profile"] = user_profile
        self.context["form"] = form

        return render(request, "users/profile.html", self.context)

    def post(self, request, username):

        user_profile = UserProfile.objects.get(username=username)
        form = UserProfileForm(
            data=request.POST, files=request.FILES, instance=user_profile
        )
        print(form.data)
        if form.is_valid():
            form.save()
            messages.success(request, "You successfully updated Profile")
            return redirect(reverse("users:profile", kwargs={"username": username}))

        else:
            messages.error(request, "You unsuccessfully updated your profile.")
            return redirect(reverse("users:profile", kwargs={"username": username}))
