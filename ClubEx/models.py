from django.db import models
from embed_video.fields import EmbedVideoField


class Video(models.Model):
    category = models.CharField(max_length=200)
    video_name = models.CharField(max_length=200)
    video = models.URLField()
    content = models.TextField()

    def __str__(self):
        return self.video_name

