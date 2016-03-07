from django.db import models
from django.contrib.auth.models import User

from account.models import Branch


class PostImages(models.Model):
    image = models.ImageField(upload_to='/post_images/')


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    images = models.ManyToManyField(PostImages)
    tags = models.ManyToManyField(User, related_name='tags')
    owner = models.ForeignKey(User)
    branch = models.ForeignKey(Branch)

    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
