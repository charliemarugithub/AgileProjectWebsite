# Generated by Django 2.2.5 on 2020-09-02 10:36

from django.db import migrations
import django.utils.timezone
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ClubEx', '0002_remove_video_stats'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='video',
            field=embed_video.fields.EmbedVideoField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
