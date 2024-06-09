from django.urls import path
from .views import UserSignUpView, UserSignInView, UserLogOutView, UserProfileView


app_name = "users"
urlpatterns = [
    path("sign_up/", UserSignUpView.as_view(), name="sign_up"),
    path("sign_in/", UserSignInView.as_view(), name="sign_in"),
    path("log_out/", UserLogOutView.as_view(), name="log_out"),
    path("profile/<str:username>", UserProfileView.as_view(), name="profile"),
]
