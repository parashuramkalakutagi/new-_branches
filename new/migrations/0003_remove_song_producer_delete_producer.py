# Generated by Django 4.1.2 on 2023-01-04 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0002_producer_song_producer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='producer',
        ),
        migrations.DeleteModel(
            name='producer',
        ),
    ]