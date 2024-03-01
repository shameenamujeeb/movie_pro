from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from movies_app.models import Movie


class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250, unique=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Profile'
        ordering = ['created']

    def __str__(self):
        return '{}'.format(self.id)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        return super().save(*args, **kwargs)


class ProfileItems(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    movie_name = models.ForeignKey(Movie, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250, unique=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        return super().save(*args, **kwargs)

    class Meta:
        db_table = 'ProfileItem'
        ordering = ['created']

    def __str__(self):
        return '{}'.format(self.movie_name)
