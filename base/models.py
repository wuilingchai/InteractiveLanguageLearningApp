from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)

    avatar = models.ImageField(null=True, default="")

    # Temporary comment this first otherwise it clash with createsuperuser command
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
