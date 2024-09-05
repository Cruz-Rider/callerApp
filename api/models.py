from django.db import models
from django.contrib.auth.models import AbstractUser

class RegisteredUser(AbstractUser):
    phone_number = models.CharField(max_length=30, unique=True)

class Contacts(models.Model):
    user = models.ForeignKey(RegisteredUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=30, unique=True)
    email = models.EmailField(blank=True)
    is_spam = models.BooleanField(default=False)

