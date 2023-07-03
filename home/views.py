from django.shortcuts import render, redirect
from . import models
# Create your views here.


def home(r):
    items = models.items.objects.all()
    return render(r,'home.html',{"items":items})


def items(r,uid):
    itemc = models.items.objects.get(uid =  uid)
    return render(r,'view.html',{'item':itemc})

def addtocart(r,uid):
    user = r.user.username
    models.Cart(uid = uid,username = user).save()
    return redirect('home/')