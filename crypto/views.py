from re import L
from django.shortcuts import render

# Create your views here.

def transaction(request):
    return render(request,"transaction.html")

def payment(request):
    return render(request,"payment.html")