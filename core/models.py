from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    followers = models.ManyToManyField('self',
                                       related_name='followers',
                                       symetrical=False)
    photo = models.ImageField(upload_to="avatar")

