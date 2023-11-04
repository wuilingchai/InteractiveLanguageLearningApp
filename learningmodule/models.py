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
    pharmacist1 = models.TextField(null=True)
    pharmacist2 = models.TextField(null=True)
    pharmacist3 = models.TextField(null=True)
    pharmacist4 = models.TextField(null=True)
    customer = models.TextField(null=False)
    customer1 = models.TextField(null=True)
    customer2 = models.TextField(null=True)
    customer3 = models.TextField(null=True)
    customer4 = models.TextField(null=True)


    def __str__(self):
        return self.location


class Restaurant(models.Model):
    location = models.CharField(max_length=200)
    waiter = models.TextField(null=False)
    waiter1 = models.TextField(null=True)
    waiter2 = models.TextField(null=True)
    waiter3 = models.TextField(null=True)
    waiter4 = models.TextField(null=True)

    customer = models.TextField(null=False)
    customer1 = models.TextField(null=True)
    customer2 = models.TextField(null=True)
    customer3 = models.TextField(null=True)
    customer4 = models.TextField(null=True)

    def __str__(self):
        return self.location
    
class Airport(models.Model):
    location = models.CharField(max_length=200)
    stewardess = models.TextField(null=False)
    stewardess1 = models.TextField(null=True)
    stewardess2 = models.TextField(null=True)
    stewardess3 = models.TextField(null=True)
    stewardess4 = models.TextField(null=True)

    customer = models.TextField(null=False)
    customer1 = models.TextField(null=True)
    customer2 = models.TextField(null=True)
    customer3 = models.TextField(null=True)
    customer4 = models.TextField(null=True)

    def __str__(self):
        return self.location
    

class Direction(models.Model):
    location = models.CharField(max_length=200)
    local = models.TextField(null=False)
    local1 = models.TextField(null=True)
    local2 = models.TextField(null=True)
    local3 = models.TextField(null=True)
    local4 = models.TextField(null=True)

    traveller = models.TextField(null=False)
    traveller1 = models.TextField(null=True)
    traveller2 = models.TextField(null=True)
    traveller3 = models.TextField(null=True)
    traveller4 = models.TextField(null=True)

    def __str__(self):
        return self.location
    
class Teatime(models.Model):
    location = models.CharField(max_length=200)
    waiter = models.TextField(null=False)
    waiter1 = models.TextField(null=True)
    waiter2 = models.TextField(null=True)
    waiter3 = models.TextField(null=True)
    waiter4 = models.TextField(null=True)

    customer = models.TextField(null=False)
    customer1 = models.TextField(null=True)
    customer2 = models.TextField(null=True)
    customer3 = models.TextField(null=True)
    customer4 = models.TextField(null=True)

    def __str__(self):
        return self.location
    
class Transportation(models.Model):
    location = models.CharField(max_length=200)
    driver = models.TextField(null=False)
    driver1 = models.TextField(null=True)
    driver2 = models.TextField(null=True)
    driver3 = models.TextField(null=True)
    driver4 = models.TextField(null=True)
    
    customer = models.TextField(null=False)
    customer1 = models.TextField(null=True)
    customer2 = models.TextField(null=True)
    customer3 = models.TextField(null=True)
    customer4 = models.TextField(null=True)
    def __str__(self):
        return self.location
# class Dialog(models.Model):
#     location = models.CharField(max_length=200)
#     person1 = models.TextField(null=False)
#     person2 = models.TextField(null=False)

#     def __str__(self):
#         return self.location