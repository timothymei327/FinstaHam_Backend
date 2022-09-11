from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Forum(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    photo_url = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='posts')
    photo_urls = ArrayField(models.CharField(max_length=200), size=10)
    caption = models.TextField(blank=False)
    hashtags = ArrayField(models.CharField(max_length=200), size=10)

    def __str__(self):
        return self.caption

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(blank=False)

    def __str__(self):
        return self.body