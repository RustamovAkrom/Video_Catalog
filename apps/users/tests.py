from django.test import TestCase
from django.urls import reverse
from apps.users.models import User


class TestUsers(TestCase):
    def setUp(self) -> None:
        user = User(
            first_name = "first_name",
            last_name = "last_name", 
            username = "username",
            email = "email",
        )
        user.set_password("2007")
        user.save()
        self.user = user

        return super().setUp()
    
    def test_urls(self):
        sign_up_response = self.client.get(reverse("users:sign_up"))
        sign_in_response = self.client.get(reverse("users:sign_in"))
        log_out_response = self.client.get(reverse("users:log_out"))
        profile_response = self.client.get(reverse("users:profile", kwargs={"username": self.user.username}))

        self.assertEqual(sign_up_response.status_code, 200)
        self.assertEqual(sign_in_response.status_code, 200)
        self.assertEqual(log_out_response.status_code, 200)
        self.assertEqual(profile_response.status_code, 302) # Authorizate

    
