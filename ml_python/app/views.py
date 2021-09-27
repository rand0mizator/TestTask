from django.shortcuts import render, redirect
from app.forms import ImageForm

import cv2
import numpy as np


def index(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            # img = cv2.imread(img_obj)
            # black = np.sum(img == 0)
            # white = np.sum(img == 255)
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})
