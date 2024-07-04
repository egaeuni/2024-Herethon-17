from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('signup/', signup, name="signup"),
    path('signup_child/', signup_child, name="signup_child"),
    path('mypage/', mypage, name='mypage'),
    path('edit_profile/', edit_profile, name="edit_profile"),
    path('', home, name="home"),
]
