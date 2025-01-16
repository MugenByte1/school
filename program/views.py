from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Program, StudentGrade, StudentExcelFile
from django.contrib.auth.decorators import login_required
from .forms import ProgramForm, StudentExcelFileForm
from django.contrib import messages
import pandas as pd
from django.conf import settings
import os
from accounts.decorators import role_required, roles_required
from accounts.models import CustomUser
from django.http import FileResponse
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import arabic_reshaper
from bidi.algorithm import get_display




@role_required
def program_add(request):
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'برنامه با موفقیت اضافه شد.')
            return redirect('program:program_view')
    else:
        form = ProgramForm()
    return render(request, 'program/program_form.html', {'form': form})



@login_required
def upload_grades(request):
    """
    آپلود فایل اکسل و ثبت نمرات در دیتابیس
    """
    if request.user.role != 'admin':
        messages.error(request, "شما دسترسی لازم را ندارید.")
        return redirect('homepage:home')

    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            student_excel = form.save()  
            file = student_excel.excel_file

            try:
                
                df = pd.read_excel(file, engine='openpyxl')

                
                if not all(col in df.columns for col in ['نام درس', 'نمره']):
                    messages.error(request, "فایل اکسل باید شامل ستون‌های 'نام درس' و 'نمره' باشد.")
                    return redirect('program:upload_grades')

                
                for _, row in df.iterrows():
                    try:
                        grade_value = float(row['نمره'])
                        StudentGrade.objects.create(
                            student=student_excel.student,
                            subject=row['نام درس'],
                            grade=grade_value
                        )
                    except ValueError:
                        messages.warning(request, f"نمره نامعتبر در ردیف {row['نام درس']}")
                        continue

                messages.success(request, f"فایل اکسل و نمرات با موفقیت ثبت شدند.")
                return redirect('program:student_grades_view')

            except Exception as e:
                messages.error(request, f"خطا در پردازش فایل: {e}")
                return redirect('program:upload_grades')

    else:
        form = ExcelUploadForm()

    return render(request, 'program/upload_grades.html', {'form': form})




@login_required
def program_add(request):
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('program:program_view')
    else:
        form = ProgramForm()
    return render(request, 'program/program_form.html', {'form': form})









@role_required('admin')
def upload_student_grades(request):
    if request.method == 'POST':
        form = StudentExcelFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'فایل نمرات با موفقیت آپلود شد.')
            return redirect('admin_dashboard')  
        else:
            messages.error(request, 'لطفا فایل را دوباره بررسی کنید.')
    else:
        form = StudentExcelFileForm()

    return render(request, 'admin/upload_student_grades.html', {'form': form})

@login_required
def student_grades_view(request):
    """
    نمایش نمرات و فایل‌های اکسل آپلود شده
    """
    if request.user.role != 'student':
        messages.error(request, "دسترسی غیرمجاز.")
        return redirect('homepage:home')

    grades = StudentGrade.objects.filter(student=request.user)
    excel_files = StudentExcelFile.objects.filter(student=request.user)

    
    if not grades.exists() and not excel_files.exists():
        messages.warning(request, "هیچ نمره‌ای یا فایل اکسل ثبت نشده است.")

    return render(request, 'program/program_student.html', {
        'grades': grades,
        'excel_files': excel_files
    })





@login_required
def program_view(request):
    user = request.user
    if user.role == 'teacher':
        programs = Program.objects.filter(teacher=user)
        return render(request, 'program/program_teacher.html', {'programs': programs})
    elif user.role == 'student':
        grades = StudentGrade.objects.filter(student=user)
        excel_files = StudentExcelFile.objects.filter(student=user)
        return render(request, 'program/program_student.html', {
            'grades': grades,
            'excel_files': excel_files
        })
    else:
        return redirect('homepage:home')







@login_required
def view_excel_file(request, file_id):
    """
    ویو برای راست‌چین کردن محتوای فایل اکسل و حذف ایندکس
    """
    file = get_object_or_404(StudentExcelFile, id=file_id)
    try:
        
        df = pd.read_excel(file.excel_file.path, engine='openpyxl')

        
        html_table = df.to_html(
            classes='table table-bordered',
            index=False,  
            justify='right'  
        )

        return render(request, 'program/view_excel_file.html', {
            'html_table': html_table,
            'file': file
        })

    except Exception as e:
        return render(request, 'program/view_excel_file.html', {
            'error': f"خطا در خواندن فایل اکسل: {e}"
        })
    


def download_excel_as_pdf(request, file_id):
    """
    ویو برای تبدیل فایل اکسل به PDF همراه با پشتیبانی کامل از متن فارسی
    """
    file = get_object_or_404(StudentExcelFile, id=file_id)

    try:
        
        df = pd.read_excel(file.excel_file.path, engine='openpyxl')

        
        pdf_path = os.path.join(settings.MEDIA_ROOT, 'converted_pdfs', f"{file.student.username}_grades.pdf")
        os.makedirs(os.path.dirname(pdf_path), exist_ok=True)

        
        font_path = os.path.join(settings.BASE_DIR, 'static/fonts/Vazir.ttf')
        pdfmetrics.registerFont(TTFont('Vazir', font_path))

        
        c = canvas.Canvas(pdf_path, pagesize=A4)
        c.setFont("Vazir", 14)

        
        student_name = f"کارنامه دانش‌آموز: {file.student.first_name} {file.student.last_name}"
        reshaped_text = arabic_reshaper.reshape(student_name)
        bidi_text = get_display(reshaped_text)
        c.drawString(100, 800, bidi_text)

        
        y_position = 750
        for index, row in df.iterrows():
            reshaped_subject = arabic_reshaper.reshape(row['نام درس'])
            reshaped_grade = arabic_reshaper.reshape(str(row['نمره']))

            
            bidi_subject = get_display(reshaped_subject)
            bidi_grade = get_display(reshaped_grade)
            c.drawString(100, y_position, f"{bidi_subject}: {bidi_grade}")
            y_position -= 20

        c.save()

        
        return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')

    except Exception as e:
        return render(request, 'program/view_excel_file.html', {
            'error': f"خطا در تبدیل فایل اکسل به PDF: {e}"
        })