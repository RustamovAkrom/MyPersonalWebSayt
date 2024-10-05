from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    bio = models.CharField(max_length=180, null=True, blank=True)
    phone_number = models.CharField(max_length=16, blank=True, null=True)
    telegram_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
    
    def __str__(self):
        return self.username