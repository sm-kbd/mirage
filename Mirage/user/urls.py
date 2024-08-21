from django.urls import path

from .views import user

urlpatterns = [path("user/<int:id>", user, name="user")]
