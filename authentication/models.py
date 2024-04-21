from django.db import models

class CustomUserModel(models.Model):
    Select =(
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ('admin', 'Admin'),
    )
    username = models.CharField(max_length=100, null = True, blank = True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
    select = models.CharField(max_length=10, choices=Select)

    def __str__(self):
        return f"{self.firstname} -> {self.lastname}"