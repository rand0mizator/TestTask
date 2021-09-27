from django.shortcuts import render
from django.views.generic import DetailView, CreateView, ListView
from django.urls import reverse_lazy

from .forms import ImageForm
from .models import Image


class HomePageView(ListView):
    model = Image
    template_name = 'images.html'
    context_object_name = 'img'


class UploadImageView(CreateView):
    model = Image
    form_class = ImageForm
    template_name = 'upload_image.html'
    success_url = reverse_lazy('images')


