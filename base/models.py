from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import JSONField

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)

    avatar = models.ImageField(null=True, default="")

    # Temporary comment this first otherwise it clash with createsuperuser command
    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class LearningData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = JSONField()

    def __str__(self):
        return f"{self.user.username}'s learning data"
    

