from tempfile import template


from django.urls import path
from django.views.generic import TemplateView

from articleapp.views import AritcleCreateView, AritcleDetailView, AritcleUpdateView, AritcleDeleteView

app_name = "articleapp"

urlpatterns = [
    path('list/', TemplateView.as_view(template_name='articleapp/list.html'), name='list'),

    path('create/', AritcleCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AritcleDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AritcleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AritcleDeleteView.as_view(), name='delete'),
]