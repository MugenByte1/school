# Generated by Django 5.1.4 on 2024-12-31 20:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentGrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('grade', models.CharField(max_length=2)),
                ('student', models.ForeignKey(limit_choices_to={'role': 'student'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('شنبه', 'شنبه'), ('یکشنبه', 'یکشنبه'), ('دوشنبه', 'دوشنبه'), ('سه\u200cشنبه', 'سه\u200cشنبه'), ('چهارشنبه', 'چهارشنبه'), ('پنج\u200cشنبه', 'پنج\u200cشنبه')], max_length=10)),
                ('period', models.CharField(choices=[('صبح', 'صبح'), ('عصر', 'عصر')], max_length=10)),
                ('teacher', models.ForeignKey(limit_choices_to={'role': 'teacher'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('teacher', 'day', 'period')},
            },
        ),
    ]
