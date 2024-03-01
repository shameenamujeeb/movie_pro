from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'category'
        verbose_name_plural ='categories'
    def __str__(self):
        return self.title
    def get_url(self):
        return reverse('movies_app:movie_by_category',args=[self.slug])
class Movie (models.Model):
    title = models.CharField(max_length=250,unique=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField()
    image=models.ImageField(upload_to="movie",blank=True)
    release_date=models.DateField()
    actors=models.CharField(max_length=250)
    language=models.CharField(max_length=250)
    genere=models.ForeignKey(Category,on_delete=models.CASCADE)
    link=models.URLField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.title)

    def __unicode__(self):
        return self.description

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title )
        return super().save(*args, **kwargs)
    def get_url1(self):
        return reverse('movies_app:movie_by_language',args=[self.slug])
class ReviewRating(models.Model):
    title=models.ForeignKey(Movie,on_delete=models.CASCADE)
    username = models.CharField(max_length=200,blank=True)
    review=models.TextField(blank=True)
    rating=models.FloatField()
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "{}".format(self.title)

