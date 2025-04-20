from tempfile import template

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic import TemplateView

from profileapp.views import ProfileCreateView, ProfileUpdateView

app_name = "articleapp"

urlpatterns = [
    path('list/', TemplateView.as_view(template_name='articleapp/list.html'), name='list'),
]