# Generated by Django 3.2.8 on 2021-10-19 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socios', '0005_auto_20211018_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagep',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]