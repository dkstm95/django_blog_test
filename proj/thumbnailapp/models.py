from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Pictures(models.Model):
    name = models.CharField(max_length=10)
    image = models.ImageField(upload_to="images", null=True)
    image_thumbnail = ImageSpecField(source='image',
        processors=[ResizeToFill(120, 80)], format='JPEG')

    def __str__(self):
        return self.name