# Generated by Django 4.1.2 on 2022-12-21 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='singer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('gender', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('singer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='song', to='new.singer')),
            ],
        ),
    ]