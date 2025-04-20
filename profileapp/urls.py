from tempfile import template

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from profileapp.views import ProfileCreateView

app_name = "profileapp"

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create'),
]