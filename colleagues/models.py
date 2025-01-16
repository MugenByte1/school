from django.db import models

class Colleague(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='colleagues/')

    def __str__(self):
        return self.name
