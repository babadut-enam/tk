from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_manajer = models.BooleanField(default=False)
    is_penonton = models.BooleanField(default=False)
    is_panitia = models.BooleanField(default=False)