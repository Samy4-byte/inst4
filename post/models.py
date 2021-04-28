from django.db import models

# Create your models here.
from django.urls import reverse_lazy





class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default='')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('post-details', kwargs={'pk': self.id})

class Category(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, primary_key=True)


    def __str__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts', null=True, blank=True)

