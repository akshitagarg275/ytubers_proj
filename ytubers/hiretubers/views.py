from django.shortcuts import render
from .models import Hiretuber
from django.contrib import messages
from django.shortcuts import render,redirect
# Create your views here.

'''
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

'''


def hiretubers(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email_id=request.POST['email']
        tuber_id=request.POST['ytuber_id']
        tuber_name=request.POST['tuber_name']
        city=request.POST['city']
        phone=request.POST['phone']
        state=request.POST['state']
        message=request.POST['message']
        user_id=request.POST['user_id']

        hiretuber=Hiretuber(first_name=first_name,last_name=last_name,email_id=email_id,tuber_id=tuber_id,tuber_name=tuber_name,city=city,phone=phone,state=state,message=message,user_id=user_id)
        hiretuber.save()
        messages.success(request,"Thanks ! for reaching us..")
        return redirect('youtubers')