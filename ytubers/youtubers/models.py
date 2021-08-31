from django.db import models
from django.db.models.base import Model
from ckeditor.fields import RichTextField

# Create your models here.

class Youtuber(models.Model):
    crew_choices=(
        ('solo','solo'),
        ('small_team','SM'),
        ('large_team','LM')
    )

    camera_choices=(
        ('canon','canon'),
        ('sony','sony'),
        ('fuji','fuji')
    )

    category_choices=(
        ('cooking','cooking'),
        ('education','education'),
        ('programming','programming'),
        ('music','music')
    )

    name=models.CharField(max_length=250)
    city=models.CharField(max_length=250)
    desc=RichTextField()
    video_url=models.CharField(max_length=200)
    crew=models.CharField(max_length=200,choices=crew_choices)
    category=models.CharField(max_length=250,choices=category_choices)
    price=models.CharField(max_length=250)
    camera_type=models.CharField(max_length=250,choices=camera_choices)
    photo=models.ImageField(upload_to='media/youtuber/%Y/%M/%d')
    age=models.IntegerField()
    height=models.IntegerField()
    subs_count=models.IntegerField()
    is_featured=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name