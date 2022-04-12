from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import logout
from pymysql import NULL
from .models import Users

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password_1 = request.POST['password']

        if Users.objects.filter(uname=username,password=password_1).exists():
            request.session['uname'] = username
            request.session['userlogged'] = True
            return render(request,"index.html")
        else:
            messages.info(request,"User not Exist")
            return redirect("login")
    else:
        return render(request,"login.html")

def index(request):
    return render(request,"index.html")

def logout(request):
    request.session['uname'] = NULL
    request.session['userlogged'] = False
    return render(request,"index.html")