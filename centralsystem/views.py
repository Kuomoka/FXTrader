from django.shortcuts import redirect, render
from accounts.models import traders
from .models import starttrader, Balances


# Create your views here.

def index(request):
    

    return render(request, "index.html")

def starttrade(request):

    newtrader = starttrader.objects.all()

    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    phonenumber = request.POST['phonenumber']
    emailadress = request.POST['emailadress']

    trader = newtrader.create(firstname=firstname, lastname=lastname, phonenumber=phonenumber,emailadress=emailadress)
    trader.save();





    return redirect('/')

