# Generated by Django 2.2.5 on 2020-09-02 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ClubEx', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='stats',
        ),
    ]