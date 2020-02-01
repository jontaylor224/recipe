from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user=models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=20)
    bio = models.TextField("Bio", null=True, blank=True)
    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    time_req = models.CharField(max_length=20)
    instructions = models.TextField("Instructions", null=True, blank=True)
    favorites = models.ManyToManyField(User, related_name='favorite', blank=True)
    def __str__(self):
        return self.title