from typing import Any
from django.shortcuts import render
from django.views import View

from _config_ import settings
from apps.users.models import UserProfile

class BaseSharedView(View):
    # Base pages configurations

    def __init__(self, **kwargs: Any) -> None:
        
        self.context = {}
        # Web Dark Mode activator
        self.context["dark_mode"] = settings.DARK_MODE
        
        super().__init__(**kwargs)
