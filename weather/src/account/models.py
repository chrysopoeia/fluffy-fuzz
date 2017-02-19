from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, blank=False, null=True)
