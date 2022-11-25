from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete= models.CASCADE)
    link = models.CharField(max_length=200)
    likes = models.ManyToManyField(User,related_name='blogposts')

    def __str__(self):
        return self.title

# Reverse function helps to continue with the created post after creating a post.
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})


