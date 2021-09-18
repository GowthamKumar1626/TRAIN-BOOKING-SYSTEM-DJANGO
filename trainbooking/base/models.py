from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import BLANK_CHOICE_DASH

class CustomUser(AbstractUser):
    class Meta:
        verbose_name = "User"
        ordering = ("username",)
    
    mobile_number = models.CharField(max_length=13, unique=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "first_name", "last_name", "mobile_number"]

    def __str__(self):
        return self.username