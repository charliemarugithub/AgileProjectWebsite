# Generated by Django 2.2.5 on 2020-09-13 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='sub_type',
            field=models.CharField(max_length=50),
        ),
    ]