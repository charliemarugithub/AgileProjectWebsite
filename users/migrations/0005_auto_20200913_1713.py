# Generated by Django 2.2.5 on 2020-09-13 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200913_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='cc_number',
            field=models.CharField(max_length=20),
        ),
    ]