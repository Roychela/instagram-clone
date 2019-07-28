from django import forms
from django.contrib.auth.models import User
from .models import Profile, Image, Comments


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ('user', )


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['image', 'commenter', 'date_posted']