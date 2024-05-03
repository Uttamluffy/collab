from django.db import models
from django.contrib.auth.models import AbstractUser

#class Student(models.Model):
#    titl=models.CharField(max_length=100)
#    description=models.CharField(max_length=100)
#    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student")


class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        TEACHER = "TEACHER", "Teacher"
        STUDENT = "STUDENT", "Student"

    username = None
    first_name = None
    last_name = None

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=20)
    phonenumber = models.CharField(max_length=20, null=True, blank=True)
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.TEACHER)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email