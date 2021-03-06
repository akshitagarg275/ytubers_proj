from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth import logout
# Create your views here.

def register(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirmpassword']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email already exists')
                    return redirect('register')
                else:
                    user=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
                    user.save()
                    messages.success(request,"Account created successfully")
                    return redirect('login')
        else:
            messages.warning(request,"Passwords do not match")
            return redirect('register')
    return render(request,'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"Logged in successfully")
            return redirect('dashboard')
        else:
            messages.warning(request,"Invalid credentials")
            return redirect('login')
    return render(request,'accounts/login.html')

def logout_user(request):
    logout(request)
    return redirect('home')

def dashboard(request):
    return render(request,'accounts/dashboard.html')