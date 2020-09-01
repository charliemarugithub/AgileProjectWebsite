from django.db import models
from embed_video.fields import EmbedVideoField


class Video(models.Model):
    category = models.CharField(max_length=200)
    video_name = models.CharField(max_length=200)
    content = models.CharField(max_length=500)
    video = EmbedVideoField()  # same like models.URLField()
    stats = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'videos'

    def __str__(self):
        return self.category

