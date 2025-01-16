# news/models.py
from django.db import models
from django.utils.text import slugify


class News(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='news/', null=True, blank=True)
    related_program = models.ForeignKey('program.Program', on_delete=models.CASCADE, null=True, blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
