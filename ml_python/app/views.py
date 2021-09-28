from django.shortcuts import render, redirect
from app.forms import ImageForm

import cv2
import numpy as np


def index(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file_in_memory = request.FILES["image"].read()
            form.save()
            img_obj = form.instance
            nparr = np.fromstring(uploaded_file_in_memory, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)
            black = np.sum(img == 0)
            white = np.sum(img == 255)
            pixel = 'черных' if black > white else 'белых'
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj, 'pixel': pixel})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})
