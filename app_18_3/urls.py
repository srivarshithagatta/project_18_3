# app_18_3/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.resume_view, name='resume'),  # Root URL for displaying the resume
]
