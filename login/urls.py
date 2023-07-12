from django.urls import path
from . import views
urlpatterns = [
    path('login',views.loginuser,name='login'),
    path('logout',views.logoutuser,name='logout/'),
    path('createuser',views.createuser,name='createuser/')
]