from __future__ import unicode_literals

from django.db import models

from core.models import User

class Home(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=200, required=True)
    body = models.TextField(required=True)
    date_created = models.DateField(required=True)

class Links(models.Model):
    ORIENTATION_CHOICES = (
        ('header', 'Header'),
        ('body', 'Body'),
        ('footer', 'Footer'),
    )
    link = models.CharField(max_length=200, required=True)
    name = models.CharField(max_length=200, required=True)
    orientation = models.CharField(max_length=10,
                            choices=ORIENTATION_CHOICES,
                            default='body')
    auto_load = models.BooleanField(default=False)
    slug = models.CharField(max_length=50, required=False,
                            unique=True)

