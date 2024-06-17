from apps.videos.models import SubscribersEmail
from django.contrib import messages
from django.shortcuts import redirect


def subscriber_email_service(request, email, redirect_url: str):
    if email is not None:
        try:
            SubscribersEmail.objects.create(email=email)
            messages.success(request, "You successfully subscribed")
            return redirect(redirect_url)
        except:
            messages.error(request, "You`r email already token")
            return redirect(redirect_url)


