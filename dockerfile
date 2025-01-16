# استفاده از تصویر پایه پایتون
FROM python:3.9-slim

# تنظیم پوشه کاری
WORKDIR /app

# کپی فایل‌های requirements
COPY requirements.txt /app/

# نصب وابستگی‌ها
RUN pip install --upgrade pip && pip install -r requirements.txt

# کپی کل پروژه
COPY . /app/

# جمع‌آوری فایل‌های استاتیک (در صورت نیاز)
RUN python manage.py collectstatic --noinput

# باز کردن پورت
EXPOSE 8000

# دستور اجرا
CMD ["gunicorn", "school.wsgi:application", "--bind", "0.0.0.0:8000"]
