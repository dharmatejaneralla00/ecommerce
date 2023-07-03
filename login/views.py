from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
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