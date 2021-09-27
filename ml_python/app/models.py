from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to='images')

    class Meta:
        db_table = "myapp_image"
