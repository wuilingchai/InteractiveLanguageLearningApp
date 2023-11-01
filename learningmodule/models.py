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


class Restaurant(models.Model):
    location = models.CharField(max_length=200)
    waiter = models.TextField(null=False)
    customer = models.TextField(null=False)

    def __str__(self):
        return self.location
    
class Airport(models.Model):
    location = models.CharField(max_length=200)
    stewardess = models.TextField(null=False)
    customer = models.TextField(null=False)

    def __str__(self):
        return self.location
    

class Direction(models.Model):
    location = models.CharField(max_length=200)
    local = models.TextField(null=False)
    traveller = models.TextField(null=False)

    def __str__(self):
        return self.location
    
class Teatime(models.Model):
    location = models.CharField(max_length=200)
    waiter = models.TextField(null=False)
    customer = models.TextField(null=False)

    def __str__(self):
        return self.location
    
class Transportation(models.Model):
    location = models.CharField(max_length=200)
    driver = models.TextField(null=False)
    customer = models.TextField(null=False)

    def __str__(self):
        return self.location
# class Dialog(models.Model):
#     location = models.CharField(max_length=200)
#     person1 = models.TextField(null=False)
#     person2 = models.TextField(null=False)

#     def __str__(self):
#         return self.location