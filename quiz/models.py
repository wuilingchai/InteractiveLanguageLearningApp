from django.db import models

# Create your models here.

class Word(models.Model):
    original_word = models.CharField(max_length=50)
    match_word = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.orignal_word} - {self.match_word}"