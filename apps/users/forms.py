from typing import Any
from django.core.exceptions import ValidationError
from django import forms
from .models import User, UserProfile
from _config_ import settings


class UserSignUpForm(forms.ModelForm):
    if settings.DARK_MODE:
        first_name = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "type": "text",
                    "name": "first_name",
                    "class": "form-control rounded-0",
                    "placeholder": "First Name",
                    "style": "background-color: rgb(10, 10, 10);",
                }
            )
        )
        last_name = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "type": "text",
                    "name": "last_ name",
                    "class": "form-control rounded-0",
                    "placeholder": "Last Name",
                    "style": "background-color: rgb(10, 10, 10);",
                }
            )
        )
        username = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "type": "text",
                    "name": "username",
                    "class": "form-control rounded-0",
                    "placeholder": "Username",
                    "style": "background-color: rgb(10, 10, 10);",
                }
            )
        )
        email = forms.EmailField(
            widget=forms.EmailInput(
                attrs={
                    "type": "email",
                    "name": "email",
                    "class": "form-control rounded-0",
                    "placeholder": "Email",
                    "style": "background-color: rgb(10, 10, 10);",
                }
            )
        )
        password1 = forms.CharField(
            widget=forms.PasswordInput(
                attrs={
                    "type": "password",
                    "name": "password1",
                    "class": "form-control rounded-0",
                    "placeholder": "Password",
                    "style": "background-color: rgb(10, 10, 10);",
                }
            )
        )
        password2 = forms.CharField(
            widget=forms.PasswordInput(
                attrs={
                    "type": "password",
                    "name": "password2",
                    "class": "form-control rounded-0",
                    "placeholder": "( Change ) Password",
                    "style": "background-color: rgb(10, 10, 10);",
                }
            )
        )

    else:
        first_name = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "type": "text",
                    "name": "first_name",
                    "class": "form-control rounded-0",
                    "placeholder": "First Name",
                }
            )
        )
        last_name = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "type": "text",
                    "name": "last_ name",
                    "class": "form-control rounded-0",
                    "placeholder": "Last Name",
                }
            )
        )
        username = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "type": "text",
                    "name": "username",
                    "class": "form-control rounded-0",
                    "placeholder": "Username",
                }
            )
        )
        email = forms.EmailField(
            widget=forms.EmailInput(
                attrs={
                    "type": "email",
                    "name": "email",
                    "class": "form-control rounded-0",
                    "placeholder": "Email",
                }
            )
        )
        password1 = forms.CharField(
            widget=forms.PasswordInput(
                attrs={
                    "type": "password",
                    "name": "password1",
                    "class": "form-control rounded-0",
                    "placeholder": "Password",
                }
            )
        )
        password2 = forms.CharField(
            widget=forms.PasswordInput(
                attrs={
                    "type": "password",
                    "name": "password2",
                    "class": "form-control rounded-0",
                    "placeholder": "( Change ) Password",
                }
            )
        )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]

    
    def save(self, commit: bool = True):
        user = super().save(commit)

        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 == password2:
            user.set_password(password2)
            user.save()
            
            return user

        else:
            raise ValidationError("Your Password must be match.")
        

class UserSignInForm(forms.Form):
    if settings.DARK_MODE:
        username = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "type": "text",
                    "name": "username",
                    "class": "form-control rounded-0",
                    "placeholder": "Username...",
                    "style": "background-color: rgb(10, 10, 10);",
                }
            )
        )
        password = forms.CharField(
            widget=forms.PasswordInput(
                attrs={
                    "type": "password",
                    "name": "password",
                    "class": "form-control rounded-0",
                    "placeholder": "Password...",
                    "style": "background-color: rgb(10, 10, 10);",
                }
            )
        )

    else:
        username = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "type": "text",
                    "name": "username",
                    "class": "form-control rounded-0",
                    "placeholder": "Username...",
                }
            )
        )
        password = forms.CharField(
            widget=forms.PasswordInput(
                attrs={
                    "type": "password",
                    "name": "password",
                    "class": "form-control rounded-0",
                    "placeholder": "Password...",
                }
            )
        )


class UserProfileForm(forms.ModelForm):
    if settings.DARK_MODE:
        bio = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "type": "text",
                    "name": "bio",
                    "class": "form-control rounded-0",
                    "placeholder": "Bio...",
                    "style": "background-color: rgb(10, 10, 10);",
                }
            ),
            required=False
        )
        first_name = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "type": "text",
                    "name": "first_name",
                    "class": "form-control rounded-0",
                    "placeholder": "First Name...",
                    "required": "",
                    "style": "background-color: rgb(10, 10, 10);",
                }
            )
        )
        last_name = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "type": "text",
                    "name": "last_name",
                    "class": "form-control rounded-0",
                    "placeholder": "Last Name...",
                    "required": "",
                    "style": "background-color: rgb(10, 10, 10);",
                }
            )
        )
        email = forms.EmailField(
            widget=forms.EmailInput(
                attrs={
                    "type": "email",
                    "name": "email",
                    "class": "form-control rounded-0",
                    "placeholder": "Email...",
                    "required": "",
                    "style": "background-color: rgb(10, 10, 10);",
                }
            )
        )
        avatar = forms.FileField(
            widget=forms.FileInput(
                attrs={"type": "file", "name": "avatar", "class": ""}
            ),
            required=False
        )

    else:
        bio = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "type": "text",
                    "name": "bio",
                    "class": "form-control rounded-0",
                    "placeholder": "Bio...",
                }
            ),
            required=False
        )
        first_name = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "type": "text",
                    "name": "first_name",
                    "class": "form-control rounded-0",
                    "placeholder": "First Name...",
                    "required": "",
                }
            )
        )
        last_name = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "type": "text",
                    "name": "last_name",
                    "class": "form-control rounded-0",
                    "placeholder": "Last Name...",
                    "required": "",
                }
            )
        ),
        email = forms.EmailField(
            widget=forms.EmailInput(
                attrs={
                    "type": "email",
                    "name": "email",
                    "class": "form-control rounded-0",
                    "placeholder": "Email...",
                    "required": "",
                }
            )
        )
        avatar = forms.FileField(
            widget=forms.FileInput(
                attrs={"type": "file", "name": "avatar", "class": ""}
            ),
            required=False
        )

    class Meta:
        model = UserProfile
        fields = ["bio", "first_name", "last_name", "email", "avatar"]


# class UserUrlForm(forms.Form):
#     if settings.DARK_MODE:
#         url = forms.URLField(
#             widget=forms.TextInput(
#                 attrs={
#                     "type": "url",
#                     "name": "url",
#                     "class": "form-control rounded-0",
#                     "placeholder": "Url...",
#                     "required": "",
#                     "style": "background-color: rgb(10, 10, 10);",
#                 }
#             )
#         )
#         description = forms.URLField(
#             widget=forms.TextInput(
#                 attrs={
#                     "type": "text",
#                     "name": "description",
#                     "class": "form-control rounded-0",
#                     "placeholder": "Description...",
#                     "style": "background-color: rgb(10, 10, 10);",
#                 }
#             ),
#             required=False
#         )

#     else:
#         url = forms.URLField(
#             widget=forms.TextInput(
#                 attrs={
#                     "type": "url",
#                     "name": "url",
#                     "class": "form-control rounded-0",
#                     "placeholder": "Url...",
#                     "required": ""
#                 }
#             )
#         )
#         description = forms.URLField(
#                     widget=forms.TextInput(
#                         attrs={
#                             "type": "text",
#                             "name": "description",
#                             "class": "form-control rounded-0",
#                             "placeholder": "Description...",
#                         }
#                     )
#                 )
        
