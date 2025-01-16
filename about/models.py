from django.db import models

class About(models.Model):
    description = models.TextField()
    objectives = models.TextField()
    image = models.ImageField(upload_to='about/', null=True, blank=True)

    def __str__(self):
        return "درباره ما"
