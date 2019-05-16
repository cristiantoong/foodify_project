from django.db import models
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default='')
    about = models.TextField(blank=True)
    location = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    profile_photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.all().create(user=kwargs['instance'])




    
post_save.connect(create_profile, sender=User)