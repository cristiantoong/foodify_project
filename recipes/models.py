from django.db import models

from django.conf import settings
from datetime import datetime

from django.contrib.auth.models import User

# class UserProfile(models.Model):
#     Name = models.CharField(max_length=200)
#     About = models.TextField(blank=True)


class Recipe(models.Model):
  #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, default=1)
  title        = models.CharField(max_length=200)
  body         = models.TextField(blank=True)
  photo_main   = models.ImageField(upload_to='photos/%Y/%m/%d')
  is_published = models.BooleanField(default=True)
  list_date    = models.DateTimeField(default=datetime.now, blank=True)
  author       = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
  
  
  def __str__(self):
    return self.title

