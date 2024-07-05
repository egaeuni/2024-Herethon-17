from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'community'
urlpatterns = [
    path('', list, name='list'),
    path('create/', create, name="create"),
    path('detail/<int:id>/', detail, name="detail"),
    path('create-answer/<int:post_id>/', create_answer, name="create-answer"),
    path('add-like/<int:post_id>/', add_like, name="add-like"),
    path('remove-like/<int:post_id>/', remove_like, name="remove-like"),
    path('add-scrap/<int:post_id>/', add_scrap, name="add-scrap"),
    path('remove-scrap/<int:post_id>/', remove_scrap, name="remove-scrap"),
    path('delete/<int:post_id>/', delete, name="delete"),
    path('delete-answer/<int:answer_id>/', delete_answer, name="delete-answer"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
