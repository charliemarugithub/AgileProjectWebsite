# Generated by Django 2.2.5 on 2020-09-02 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClubEx', '0004_auto_20200902_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='content',
            field=models.TextField(),
        ),
    ]
