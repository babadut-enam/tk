from django.db import models
from django.contrib.auth.models import AbstractUser,User

# Create your models here.
class User(AbstractUser):
    is_manajer = models.BooleanField(default=False)
    is_penonton = models.BooleanField(default=False)
    is_panitia = models.BooleanField(default=False)

    # class Role(models.TextChoices):
    #     MANAJER = "MANAJER", 'Manajer'
    #     PENONTON = "PENONTON", 'Penonton'
    #     PANITIA = "PANITIA", 'Panitia'
    
    # role = models.CharField('Role')
