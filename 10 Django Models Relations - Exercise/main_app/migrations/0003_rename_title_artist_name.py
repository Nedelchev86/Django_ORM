# Generated by Django 4.2.4 on 2023-11-12 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_song_artist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='title',
            new_name='name',
        ),
    ]
