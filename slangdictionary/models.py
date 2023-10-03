from django.db import models

# Create your models here.
class Slang(models.Model):
    name = models.CharField(max_length=200)
    definition = models.TextField(null=False)

    def __str__(self):
        return self.name