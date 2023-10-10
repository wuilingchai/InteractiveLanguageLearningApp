from django.db import models

# Create your models here.

class Word(models.Model):
    original_word = models.CharField(max_length=50)
    match_word = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.original_word} - {self.match_word}"
    

class Choices(models.Model):
    question = models.TextField(max_length=200)
    answer = models.CharField(max_length=50)
    choice1 = models.CharField(max_length=50)
    choice1 = models.CharField(max_length=50)
    choice1 = models.CharField(max_length=50)
    choice1 = models.CharField(max_length=50)

    def __str__(self):
        return self.question
