from django.db import models
from datetime import datetime

# Create your models here.
class Addpolicy(models.Model):
    created=models.DateTimeField(default=datetime.now(),blank=True)
    policynames=models.CharField(max_length=50)

    def __str__(self) :
        return self.policynames

class Login(models.Model):
    userType=models.CharField(max_length=20,default='U',blank=True)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=20)
    email=models.EmailField(default=None)
    city=models.CharField(max_length=20,default=None)
    mobile=models.BigIntegerField(default=None)

    def __str__(self) :
        return (f'{self.userType},{self.username},{self.password}')

class policyTable(models.Model):
    created=models.DateTimeField(default=datetime.now(),blank=True)
    Name=models.CharField(max_length=30)
    policyName=models.ForeignKey(Addpolicy,null=True,default=None,on_delete=models.CASCADE)
    policyTenure=models.SmallIntegerField(default=None)
    totalAmount=models.IntegerField(default=123456)
    premiumAmount=models.BigIntegerField(default=None)
    premiumPay=models.TextField(default=None)
    expectedReturn=models.BigIntegerField(default=None)

    def __str__(self):
        return self.policyName

