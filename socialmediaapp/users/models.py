from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    following = models.ManyToManyField(User, related_name='following', blank=True)


    def __str__(self):
        return f'{self.user.username}'

    def profiles_posts(self):
        return self.post_set.all()



