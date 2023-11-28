from django.db import models

# Create your models here.

class Word(models.Model):
    original_word = models.CharField(max_length=50)
    match_word = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.original_word} - {self.match_word}"
    

class Choices(models.Model):
    div_id = models.CharField(max_length=256, null=True, blank=True)
    question = models.TextField(max_length=200)
    answer = models.CharField(max_length=50)
    choice1 = models.CharField(max_length=50, null=True, blank=True)
    choice2 = models.CharField(max_length=50, null=True, blank=True)
    choice3 = models.CharField(max_length=50, null=True, blank=True)
    choice4 = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.question

