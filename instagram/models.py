from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Image(models.Model):
    image_name = models.CharField(max_length=100)
    image_caption = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'images/', blank = True)

    def __str__(self):
        return self.image_name