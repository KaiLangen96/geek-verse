from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_help_center, name="view_help_center"),
]
