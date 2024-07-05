from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('signup/', signup, name="signup"),
    path('signup_child/', signup_child, name="signup_child"),
    path('mypage/', mypage, name='mypage'),
    path('mypage/posts/', post_number, name='post_number'),
    path('mypage/scrap/post/', scrap_post, name='scrap_post'),
    path('mypage/scrap/policy/', scrap_policy, name='scrap_policy'),
    path('mypage/scrap/program/', scrap_program, name='scrap_program'),
    path('edit_profile/', edit_profile, name="edit_profile"),
    path('', home, name="home"),
]