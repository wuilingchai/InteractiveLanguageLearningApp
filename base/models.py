from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


# Create your models here.

# class User(AbstractUser):
#     name = models.CharField(max_length=200, null=True)
#     email = models.EmailField(unique=True, null=True)

#     avatar = models.ImageField(null=True, default="")

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
