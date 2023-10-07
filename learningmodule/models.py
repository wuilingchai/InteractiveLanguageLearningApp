from django.db import models

# Create your models here.
class Vocabulary(models.Model):
    name = models.CharField(max_length=200)
    definition = models.TextField(null=False)
    pronunciation = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Pharmacy(models.Model):
    location = models.CharField(max_length=200)
    pharmacist = models.TextField(null=False)
    customer = models.TextField(null=False)

    def __str__(self):
        return self.location

# class Dialog(models.Model):
#     location = models.CharField(max_length=200)
#     person1 = models.TextField(null=False)
#     person2 = models.TextField(null=False)

#     def __str__(self):
#         return self.location