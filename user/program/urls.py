from django.urls import path
from .views import program_home, program_list, policy_list, policy_detail, program_detail, add_scrap, remove_scrap

app_name = 'program'

urlpatterns = [
    path('', program_home, name='program_home'),
    path('list/', program_list, name='program_list'),
    path('policies/', policy_list, name='policy_list'),
    path('policies/<int:policy_id>/', policy_detail, name='policy_detail'),
    path('programs/<int:program_id>/', program_detail, name='program_detail'),
    path('scrap/add/<int:policy_id>/', add_scrap, name='add_scrap'),
    path('scrap/remove/<int:policy_id>/', remove_scrap, name='remove_scrap'),
]
