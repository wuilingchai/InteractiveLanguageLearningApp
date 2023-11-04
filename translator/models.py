from django.db import models
# need to use your own user modle not from django.auth
from base.models import User

class TranslationHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    source_text = models.TextField()
    source_language = models.CharField(max_length=20)
    trans_text = models.TextField()
    trans_language = models.CharField(max_length=20)
