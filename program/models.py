from django.db import models
from django.conf import settings

class Program(models.Model):
    DAYS_OF_WEEK = [
        ('شنبه', 'شنبه'),
        ('یکشنبه', 'یکشنبه'),
        ('دوشنبه', 'دوشنبه'),
        ('سه‌شنبه', 'سه‌شنبه'),
        ('چهارشنبه', 'چهارشنبه'),
        ('پنج‌شنبه', 'پنج‌شنبه'),
    ]

    PERIOD_CHOICES = [
        ('صبح', 'صبح'),
        ('عصر', 'عصر'),
    ]

    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'role': 'teacher'})
    day = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    period = models.CharField(max_length=10, choices=PERIOD_CHOICES)

    class Meta:
        unique_together = ('teacher', 'day', 'period')

    def __str__(self):
        return f"{self.teacher} - {self.day} - {self.period}"






class StudentExcelFile(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    excel_file = models.FileField(upload_to='student_grades/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} - {self.excel_file.name}"


class StudentGrade(models.Model):
    """
    نمرات دانش‌آموز به همراه نام درس و نمره
    """
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        limit_choices_to={'role': 'student'}
    )
    subject = models.CharField(max_length=100)
    grade = models.FloatField()

    def __str__(self):
        return f"{self.student.username} - {self.subject}: {self.grade}"