from django.contrib import admin
from .models import Balances, systemUsers
from accounts.models import traders

# Register your models here.

admin.site.register(Balances)
