from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=30, null=True, blank=True)


class Resource(models.Model):
    title = models.CharField(max_length=100, unique=True, null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField(max_length=200, unique=True, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True, related_name="resources")
    cover = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return f"{self.title} by {self.author}"


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()

    def __str__(self):
        return f"{self.title}"
    

class Favorite(models.Model):
    resource = models.ForeignKey('Resource', on_delete=models.CASCADE, blank=True, null=True, related_name="favorites")
    user = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True, related_name="favorites")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

