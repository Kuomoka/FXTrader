import email
from django.db import models

# Create your models here.


class carddetails(models.Model):
    
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    card_name = models.CharField(max_length=100)
    card_number = models.BigIntegerField()
    exp_month = models.IntegerField()
    exp_year = models.IntegerField()
    cvv = models.IntegerField()

class BTCPayments(models.Model):
    paymentcode = models.CharField(max_length=100)
    amount = models.BigIntegerField()
    paymentemail = models.CharField(max_length=100)
       