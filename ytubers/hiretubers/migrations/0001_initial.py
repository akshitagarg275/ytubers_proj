# Generated by Django 3.2.9 on 2021-11-28 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hiretuber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email_id', models.EmailField(max_length=200)),
                ('tuber_id', models.IntegerField()),
                ('tuber_name', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
