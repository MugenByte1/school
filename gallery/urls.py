from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.gallery_list, name='gallery_list'),
    path('add/', views.gallery_add, name='gallery_add'),
    path('edit/<int:pk>/', views.gallery_edit, name='gallery_edit'),
    path('delete/<int:pk>/', views.gallery_delete, name='gallery_delete'),
]
