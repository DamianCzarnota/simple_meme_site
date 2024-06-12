from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment, Image

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","password1", "password2"]

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']