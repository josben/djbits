from __future__ import unicode_literals

from django.db import models
from core.models import User

class Blog(models.Model):
    title = models.CharField(max_length=100, required=True)
    date_created = models.DateField(required=True)

class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts')
    blog = models.ForeignKey(Blog)
    title = models.CharField(max_length=255, required=True)
    body = models.TextField(blank=True, null=True)

class Photo(models.Model):
    post = models.ForeignKey(Post, related_name='photos')
    image = models.ImageField(upload_to="%Y/%m/%d")
