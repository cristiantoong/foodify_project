from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.db import models
from . import models
from .models import UserProfile

# class SignUpForm(UserCreationForm):
#     class Meta:
#         model = UserImage
#         fields = ('photo_profile',)


# photo_profile   = models.ImageField(upload_to='photos/%Y/%m/%d')


class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
        )

class PhotoProfileUpload(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_photo',)
        