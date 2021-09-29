from django.shortcuts import render, redirect
from .forms import ImageForm
from .utils import count_pixels

from PIL import ImageColor


def index(request):
    if request.method == 'POST':
        color = '#' + request.POST["color"]
        try:
            color = ImageColor.getrgb(color)
        except ValueError:
            color = None
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['image']
            print(type(uploaded_file))
            form.save()
            img_obj = form.instance
            black = count_pixels(uploaded_file, (0, 0, 0))
            white = count_pixels(uploaded_file, (255, 255, 255))
            pixel_count = count_pixels(uploaded_file, color)
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj, 'pixel_count': pixel_count,
                                                  'white': white, 'black': black, 'color': color})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})
