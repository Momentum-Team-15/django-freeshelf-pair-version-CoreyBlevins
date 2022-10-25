from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=30, null=True, blank=True)
    
class Resources(models.Model):
    title = models.CharField(max_length=100, unique=True, null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField(max_length=200, unique=True, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
