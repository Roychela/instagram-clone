from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class Image(models.Model):
    image_name = models.CharField(max_length=100)
    image_caption = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'images/', blank = True)

    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()

    def __str__(self):
        return self.image_name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)


    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()

    @classmethod
    def search_profile(cls, name):
        profile = Profile.objects.filter(user__username__icontains = name)
        return profile

    def __str__(self):
        return f'{self.user.username} Profile'


class Comments(models.Model):
    comment = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_comment(self):
        self.save()
    def delete_comment(self):
        self.delete()
    def __str__(self):
        return str(self.comment)
    
    @classmethod
    def get_comments_by_images(cls, id):
        comments = Comments.objects.filter(image__pk = id)
        return comments