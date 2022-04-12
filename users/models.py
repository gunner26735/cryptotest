from django.db import models

# Create your models here.

class Users(models.Model):
    uname = models.CharField(max_length=50)
    mobileno = models.IntegerField(max_length=10)
    walletaddress = models.CharField(max_length=50)
    password = models.CharField(max_length=18)

# class Verifier(models.Model):
#     otp_verification = models.BooleanField(default=False)
#     uname = models.ForeignKey(Users,on_delete=models.CASCADE)