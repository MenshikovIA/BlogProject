from django.db import models
from django.contrib.auth.models import User


class MyUser(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profile_pics/', blank=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts')
    title = models.CharField(max_length=100)
    text = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='attachments/', blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    text = models.CharField(max_length=65536)
    creation_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.text[:15]
