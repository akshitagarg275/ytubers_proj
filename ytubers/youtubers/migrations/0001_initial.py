# Generated by Django 3.2.6 on 2021-08-20 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Youtuber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
                ('desc', models.TextField()),
                ('video_url', models.CharField(max_length=200)),
                ('crew', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=250)),
                ('price', models.CharField(max_length=250)),
                ('camera_type', models.CharField(max_length=250)),
                ('photo', models.ImageField(upload_to='media/youtuber/%Y/%M/%d')),
                ('age', models.IntegerField()),
                ('height', models.IntegerField()),
                ('subs_count', models.IntegerField()),
                ('is_featured', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
