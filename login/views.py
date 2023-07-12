from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.


def loginuser(r):
    if  not r.user.is_authenticated:
        if r.method == 'POST':
            usename = r.POST['username']
            password = r.POST['password']
            user = authenticate(username = usename,password=password)
            if user:
                login(r,user)
                messages.success(r,'User login successful')
                return  redirect('home/')
            else:
                messages.error(r,'User not found')
                return render(r,'login.html')
        else:
            return render(r,'login.html')
    else:
        return redirect('home/')

def logoutuser(request):
    logout(request)
    messages.success(request,"Logout Successful")
    return render(request,'login.html')

def createuser(r):
    if r.method == 'POST':
        username = r.POST['username']
        password = r.POST['password']
        name = r.POST['name']
        if User.objects.filter(username = username).exists():
            messages.error(r,'username alrady exists')
            return  render(r,'add uuser.html')
        else:
            user = User.objects.create_user(username = username,password=password)
            user.first_name = name
            user.save()
            return redirect('home/')
    return render(r,'add uuser.html')