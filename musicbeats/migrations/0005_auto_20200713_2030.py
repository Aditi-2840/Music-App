# Generated by Django 3.0.8 on 2020-07-13 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicbeats', '0004_auto_20200713_2014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='video_id',
            new_name='music_id',
        ),
    ]