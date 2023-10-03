from django.db import models

# Create your models here.
class Vocabulary(models.Model):
    name = models.CharField(max_length=200)
    definition = models.TextField(null=False)
    pronunciation = models.CharField(max_length=200)

    def __str__(self):
        return self.name