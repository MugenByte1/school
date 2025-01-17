# Generated by Django 5.1.4 on 2024-12-31 22:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('program', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='news/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('related_program', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='program.program')),
            ],
        ),
    ]
