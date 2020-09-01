from django.db import models

class Video(models.Model):
    category = models.CharField(max_length=200)
    video_name = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    stats = models.CharField(max_length=100)
    
 
