from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name = 'home/'),
    path('items/<str:uid>',views.items,name= 'items/'),
    path('adddtocart/<str:uid>',views.addtocart,name = 'addtocart/'),
    path('additems',views.additem,name = 'additems/'),
    path('delete/<str:uid>',views.deleteitem,name='delete/')
]