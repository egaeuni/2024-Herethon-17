from django.urls import path
from .views import program_home, program_list, policy_list, policy_detail, program_detail, add_scrap_policy, remove_scrap_policy, add_scrap_program, remove_scrap_program

app_name = 'program'

urlpatterns = [
    path('', program_home, name='program_home'),
    path('list/', program_list, name='program_list'),
    path('policies/', policy_list, name='policy_list'),
    path('policies/<int:policy_id>/', policy_detail, name='policy_detail'),
    path('programs/<int:program_id>/', program_detail, name='program_detail'),
    path('scrap/policy/add/<int:policy_id>/', add_scrap_policy, name='add_scrap_policy'),
    path('scrap/policy/remove/<int:policy_id>/', remove_scrap_policy, name='remove_scrap_policy'),
    path('scrap/program/add/<int:program_id>/', add_scrap_program, name='add_scrap_program'),
    path('scrap/program/remove/<int:program_id>/', remove_scrap_program, name='remove_scrap_program'),
]
