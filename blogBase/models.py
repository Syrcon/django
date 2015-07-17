# coding: utf-8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User)
    datetime = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=10000)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["-datetime"]

    def get_absolute_url(self):
        return "/blog/%i/" % self.id

class Comment(models.Model):
    author = models.ForeignKey(User)
    datetime = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=2000)
    post = models.ForeignKey(Post)

    def __unicode__(self):
        return self.content