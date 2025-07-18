from django.db import models
from django.contrib.auth.models import AbstractUser

class TelegramUser(AbstractUser):
    telegram_id = models.BigIntegerField(unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(unique=True, max_length=255, blank=True, null=True)
    language_code = models.CharField(max_length=10)
    is_premium = models.BooleanField(default=False)
    avatar = models.CharField(max_length=255, default='Av01.jpg')
    points = models.IntegerField(default=0)
    streak = models.IntegerField(default=0)
    time_spent = models.IntegerField(default=0)  # in minutes
    
    def __str__(self):
        return f"{self.first_name} (@{self.username})"

