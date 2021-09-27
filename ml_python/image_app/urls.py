from django.contrib import admin
from django.urls import path

from .views import HomePageView, UploadImageView

urlpatterns = [
    path('images', HomePageView.as_view(), name='images'),
    path('', UploadImageView.as_view(), name='upload_image'),
]
