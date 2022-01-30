from django.urls import path
from . import views

urlpatterns = [
    path('cardpayment', views.cardpayment, name='cardpayment'),
    path("invest", views.invest, name="invest"),
    path("BTCpayment", views.BTCpayment, name="BTCpayment"),
    path("logout",views.logout,name="logout"),
    path("login",views.logout,name="login"),
]