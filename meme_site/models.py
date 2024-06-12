from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ForeignKey('Image', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.created_at.strftime('%Y-%m-%d %H:%M')}"

class Image(models.Model):
    image = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='liked_images', blank=True)

    def __str__(self):
        return self.title
