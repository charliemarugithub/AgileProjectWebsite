# Generated by Django 2.2.5 on 2020-09-02 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClubEx', '0003_video_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.URLField(),
        ),
    ]