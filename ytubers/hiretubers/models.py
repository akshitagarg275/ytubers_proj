from django.db import models

# Create your models here.

class Hiretuber(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email_id=models.EmailField(max_length=200)
    tuber_id=models.IntegerField()
    tuber_name=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    message=models.TextField()
    user_id=models.IntegerField(blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email_id
