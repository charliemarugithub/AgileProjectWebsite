from django.db import models
from embed_video.fields import EmbedVideoField


class Video(models.Model):
    category = models.CharField(max_length=200)
    video_name = models.CharField(max_length=200)
    video = EmbedVideoField()
    content = models.TextField()
    video_views = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        ordering = ('-video_name',)

    def __str__(self):
        return self.video_name