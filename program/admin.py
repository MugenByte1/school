# program/admin.py
from django.contrib import admin
from .models import Program, StudentGrade,StudentExcelFile, StudentGrade

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'day', 'period')
    list_filter = ('day', 'period')
    search_fields = ('teacher__username',)

# @admin.register(StudentGrade)
# class StudentGradeAdmin(admin.ModelAdmin):
#     list_display = ('student', 'subject', 'grade')
#     list_filter = ('subject',)
#     search_fields = ('student__username', 'subject')
#



admin.site.register(StudentExcelFile)

class StudentGradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'grade')

admin.site.register(StudentGrade, StudentGradeAdmin)
