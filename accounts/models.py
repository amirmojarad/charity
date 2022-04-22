from django.contrib.auth.models import AbstractUser
from django.db import models

class GenderChoices(models.Choices):
    Female = "F"
    Male = "M"
    


class User(AbstractUser):
    address = models.TextField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GenderChoices.choices, null=True, blank=True)
    
