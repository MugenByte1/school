from django.urls import path
from . import views

app_name = 'program'

urlpatterns = [
    path('add/', views.program_add, name='program_add'),
    path('upload_grades/', views.upload_grades, name='upload_grades'),
    path('view/', views.program_view, name='program_view'),
    path('upload-student-grades/', views.upload_student_grades, name='upload_student_grades'),
    path('student-grades/', views.student_grades_view, name='student_grades_view'),
    path('view-excel/<int:file_id>/', views.view_excel_file, name='view_excel_file'),  
    path('download-pdf/<int:file_id>/', views.download_excel_as_pdf, name='download_excel_as_pdf'),

    
]
