from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models
from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete= models.CASCADE)
    link = models.CharField(max_length=200)
    likes = models.ManyToManyField(User,related_name='blogposts', blank=True)
    saving = models.ManyToManyField(User, related_name='saving', blank=True)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title

# Reverse function helps to continue with the created post after creating a post.
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})


class Comment(models.Model):
    post =  models.ForeignKey(Post,related_name="comments", on_delete= models.CASCADE)
    name = models.ForeignKey(User,on_delete= models.CASCADE,default=1)
    body = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date_added']
    def __str__(self):
        return self.post.title