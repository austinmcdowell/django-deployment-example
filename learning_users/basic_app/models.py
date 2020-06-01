from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional classes
    portfolio_site = models.URLField(blank=True) #blank=True means can be empty
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True) #profile_pics is subdirectory of Media folder

    def __str__(self):
        return self.user.username
