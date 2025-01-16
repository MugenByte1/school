from django import forms
from .models import Program,StudentExcelFile, StudentGrade
from django.conf import settings
from django.contrib.auth import get_user_model

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['teacher', 'day', 'period']


class StudentExcelFileForm(forms.ModelForm):
    class Meta:
        model = StudentExcelFile
        fields = ['student', 'excel_file']



class ExcelUploadForm(forms.Form):
    student = forms.ModelChoiceField(
        queryset=get_user_model().objects.filter(role='student'),
        label="انتخاب دانش‌آموز"
    )
    grades_file = forms.FileField(label="آپلود فایل اکسل")