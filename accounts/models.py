from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.timezone import now


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, national_code, first_name, last_name, role, **other_fields):
        if not username:
            raise ValueError('The Username must be set')
        user = self.model(
            username=username,
            national_code=national_code,
            first_name=first_name,
            last_name=last_name,
            role=role,
            **other_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, national_code, first_name, last_name, role='admin', **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, national_code, first_name, last_name, role, **other_fields)





class CustomUser(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    username = models.CharField(max_length=150, unique=True)
    national_code = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=now)  

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['national_code', 'first_name', 'last_name', 'role']

    def __str__(self):
        return self.username
