from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('signup_child/', views.signup_child, name="signup_child"),
    path('mypage/', views.mypage, name='mypage'),
    path('home/', views.home, name="home"),
]