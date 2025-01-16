from django.urls import path
from . import views

app_name = 'colleagues'

urlpatterns = [
    path('', views.colleagues_list, name='colleagues_list'),
    path('add/', views.colleague_add, name='colleague_add'),
    path('edit/<int:pk>/', views.colleague_edit, name='colleague_edit'),
    path('delete/<int:pk>/', views.colleague_delete, name='colleague_delete'),
]
