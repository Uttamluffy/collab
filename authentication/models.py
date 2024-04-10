# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from .managers import CustomUserManager

# class CustomUSer(AbstractUser):
#     ROLE_CHOICES = [
#         ('ST', 'Student'),
#         ('ST', 'Teacher'),
#     ]
    
#     role = models.CharField(max_length=2, choices=ROLE_CHOICES)

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = []

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email

from django.db import models
from django.contrib.auth.models import User


class Subject(models.Model):
    subject_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.subject_name
    

class SubjectTeacher(models.Model):
    subject = models.OneToOneField(Subject, on_delete=models.CASCADE, related_name='subject')
    teacher = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher')

    def __str__(self):
        return f'{self.subject.subject_name} - {self.teacher.first_name} {self.teacher.last_name}'