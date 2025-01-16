from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.contact_view, name='contact'),
    path('edit/', views.contact_edit, name='contact_edit'),
]
