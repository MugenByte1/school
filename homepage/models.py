from django.db import models

class HomePage(models.Model):
    welcome_image = models.ImageField(upload_to='homepage/')
    welcome_text = models.TextField(default='خوش آمدید به سیستم مدیریت مدرسه هوشمند اما علی(ع)')

    def __str__(self):
        return "صفحه اصلی"
