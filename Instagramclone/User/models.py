from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserModel(AbstractUser):
    id = models.IntegerField(primary_key=True)
    display_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=255, blank=False)
    website = models.URLField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    bio = models.TextField(blank=True, null=True)
    followers = models.ManyToManyField('UserModel', related_name='followings', blank=True, symmetrical=False)

    def profile_pic_url(self):
        if self.profile_pic and hasattr(self.profile_pic, 'url'):
            return self.profile_pic.url
        else:
            return '/static/images/default-avatar.png'

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'AppUsers'