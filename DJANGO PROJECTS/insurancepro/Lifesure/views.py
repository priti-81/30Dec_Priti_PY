from django.shortcuts import render,redirect
from .forms import loginForm,signupForm,userpolicyForm,policyForm
from .models import Login,Addpolicy,policyTable
from django.contrib.auth import logout
from django.db.models import Sum,Count

# Create your views here.

def index(request):
    data=Addpolicy.objects.all()
    cuser=policyTable.objects.count()
    Tpolicy=Addpolicy.objects.count()
    fund=policyTable.objects.aggregate(Sum('totalAmount'))
    fund1=fund['totalAmount__sum']
    if request.method=="POST":
        add=policyForm(request.POST)
        if add.is_valid():
            add.save()
    return render(request,"index.html",{'data1':data,'cuser':cuser,"tpolicy":Tpolicy,'fund1':fund1})



def login(request):
    if request.method=='POST':
        newuser=loginForm(request.POST)
        unm=request.POST['username']
        pas=request.POST['password']
 
        uservalue=Login.objects.filter(username=unm,password=pas).values()
        id=uservalue[0]['id']
        ut=uservalue[0]['userType']
        print(id)
   
        if ut == 'A':
            return redirect ('admin')
        else:
            return redirect('policy')
    return render(request,"login.html")



def signup(request):
    if request.method=='POST':
        newuser=signupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            return redirect ('login')
        else:
            print(newuser.errors)
    return render(request,"signup.html")



def policy(request):
    data=Addpolicy.objects.all()
    if request.method=='POST':
        userForm=userpolicyForm(request.POST)
        if userForm.is_valid():
            userForm.save()
        else:
            print(userForm.errors)
    return render(request,"policy.html",{'data1':data})



def userlogout(request):
    logout(request)
    return redirect("login")



def deletedata(request,id):
    deleteU=Addpolicy.objects.get(id=id)
    Addpolicy.delete(deleteU)
    return redirect("admin")
