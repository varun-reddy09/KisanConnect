from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('loginform/', views.loginform, name='loginform'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),

    path('dashboard/',views.dashboard,name='dashboard'),
    path('cropinfo/',views.cropinfo,name='cropinfo'),
    path('marketprice/', views.marketprice, name='marketprice'),

]