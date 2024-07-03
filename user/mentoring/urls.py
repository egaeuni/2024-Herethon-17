from django.urls import path
from .views import *


app_name = 'mentoring'
urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:id>/', detail, name = 'detail'),
    path('question/<int:mento_id>', question, name="question"),
    path('search/', search, name="search"),
    path('record-sheet/', record_sheet, name="record-sheet"),
    path('sheet-list/', sheet_list, name='sheet-list')
]
