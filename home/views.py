from django.shortcuts import render, redirect
from . import models
# Create your views here.
from .forms import AddItem

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

def additem(r):
    if r.method == 'POST':
        uid = r.POST['uid']
        name = r.POST['name']
        price = r.POST['price']
        availability = r.POST['avalability']
        des = r.POST['des']
        rating = r.POST['rating']
        models.items(uid = uid,name = name,price=price,avalability=availability,des=des,rating=rating).save()
    return render(r,'additems.html',{"form":AddItem})

def deleteitem(r,uid):
    models.items.objects.get(uid=uid).delete()
    return redirect('home/')