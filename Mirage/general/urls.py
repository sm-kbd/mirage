from django.urls import path, include
from .views import register, logout
from django.contrib.auth.views import LoginView

urlpatterns = [
        path("register/", register),
        path("logout/", logout),
        path("login/", LoginView.as_view(template_name="login.html"))
        ]
