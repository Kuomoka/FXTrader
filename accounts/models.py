from django.db import models

# Create your models here.

class traders(models.Model):
    
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    physical_adress = models.CharField(max_length=100)
    Balance = models.CharField(max_length=100)

