from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('<slug:slug>/', views.news_detail, name='news_detail'),
    path('add/', views.news_add, name='news_add'),
    path('edit/<int:pk>/', views.news_edit, name='news_edit'),
    path('delete/<int:pk>/', views.news_delete, name='news_delete'),
]
