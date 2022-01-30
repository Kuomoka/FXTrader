from django.db import models

# Create your models here.


class systemUsers(models.Model):
    
    email = models.CharField(max_length=100)
    Balance = models.CharField(max_length=100)

class Balances(models.Model):
    
    email = models.CharField(max_length=100)
    Balance = models.CharField(max_length=100)
       
class starttrader(models.Model):
    
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    emailadress = models.CharField(max_length=100)
    phonenumber = models.BigIntegerField()