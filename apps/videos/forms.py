from django import forms
from apps.videos.models import Categories
from _config_ import settings


def CATEGORY_CHOICES() -> list:
    choices = []
    for category in Categories.objects.all():
        choices.append((str(category).lower(), str(category).title()))
    return choices


class VideoCreateForm(forms.Form):
    if settings.DARK_MODE:
        title = forms.CharField(widget=forms.TextInput(attrs={
            "type":"text", "name": "title", "class": "form-control rounded-0", "placeholder":"Title...", "required":"", "style": "background-color: rgb(10, 10, 10);",
        }))
        photo = forms.ImageField(widget=forms.FileInput(attrs={
            "type":"file", "name": "photo", "placeholder":"Photo...", "required":"", "style": "color: white;",
        }))
        video = forms.FileField(widget=forms.FileInput(attrs={
            "type":"file", "name": "video", "placeholder":"Video...", "required":"", "style": "color: white;",
        }))
        description = forms.CharField(widget=forms.TextInput(attrs={
            "type":"text", "name": "description", "class": "form-control rounded-0", "placeholder":"Description...", "required":"", "style": "background-color: rgb(10, 10, 10);",
        }))
        content = forms.CharField(widget=forms.Textarea(attrs={
            "rows":"8", "name": "content", "class": "form-control rounded-0", "placeholder":"Content...", "required":"", "style": "background-color: rgb(10, 10, 10);",
        }))
        category = forms.ChoiceField(choices=CATEGORY_CHOICES())


    else:
        title = forms.CharField(widget=forms.TextInput(attrs={
            "type":"text", "name": "title", "class": "form-control rounded-0", "placeholder":"Title...", "required":""
        }))
        photo = forms.ImageField(widget=forms.FileInput(attrs={
            "type":"file", "name": "photo", "placeholder":"Photo...", "required":""
        }))
        video = forms.FileField(widget=forms.FileInput(attrs={
            "type":"file", "name": "video", "placeholder":"Video...", "required":""
        }))
        description = forms.CharField(widget=forms.TextInput(attrs={
            "type":"text", "name": "description", "class": "form-control rounded-0", "placeholder":"Description...", "required":""
        }))
        content = forms.CharField(widget=forms.Textarea(attrs={
            "rows":"8", "name": "content", "class": "form-control rounded-0", "placeholder":"Content...", "required":""
        }))
        category = forms.ChoiceField(choices=CATEGORY_CHOICES())
    # is_active = forms.BooleanField()