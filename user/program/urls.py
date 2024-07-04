from django.urls import path
from .views import program_home, program_list, policy_list

app_name = 'program'

urlpatterns = [
    path('', program_home, name='program_home'),
    path('program/', program_list, name='program_list'),
    path('policies/', policy_list, name='policy_list'),  
]
