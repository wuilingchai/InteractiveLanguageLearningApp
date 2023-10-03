from django.db import models

# Create your models here.
class TranslationHistory(models.Model):
    source_text = models.TextField()
    source_language = models.CharField(max_length=20)
    trans_text = models.TextField()
    trans_language = models.CharField(max_length=20)
    