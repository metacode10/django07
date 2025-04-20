from tempfile import template

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from profileapp.views import ProfileCreateView, ProfileUpdateView

app_name = "profileapp"

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create'),
    path('update/<int:pk>', ProfileUpdateView.as_view(), name='update'),
]