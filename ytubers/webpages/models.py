from django.db import models

# Create your models here.
class Slider(models.Model):
    headline=models.CharField(max_length=200)
    subtitle=models.CharField(max_length=200)
    button_text=models.CharField(max_length=200)
    photo=models.ImageField(upload_to='media/slider/%Y/%m')
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline
class Team(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    role=models.CharField(max_length=200)
    fb_link=models.CharField(max_length=200)
    insta_link=models.CharField(max_length=200)
    photo=models.ImageField(upload_to='media/team/%Y/%m/%d')
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
