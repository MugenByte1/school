from django.db import models

class Contact(models.Model):
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return "تماس با ما"
