from django.db import models
from PIL import Image as pil_image


class Image(models.Model):
    image = models.ImageField(upload_to='images')

    # def save(self):
    #     print("Saving image")
    #     super().save()
    #
    #     img = pil_image.open(self.image.path)
    #     if img.height > 500 or img.width > 500:
    #         new_img = (500, 500)
    #         img.thumbnail(new_img)
    #         img.save(self.image.path)
