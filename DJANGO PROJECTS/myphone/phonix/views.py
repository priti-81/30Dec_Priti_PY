from django.shortcuts import render,redirect
from .forms import productForm
from .models import product,productdetails

# Create your views here.
def index(request):
    # data=productdetails.objects.all()
    data1=product.objects.all()
    # print(data)
    if request.method =='POST':
        form=productForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            print('data saved successfully')
        else:
            print(productForm.errors)
    return render (request,'index.html',{'data1': data1})

def showdata(request):
    get_data=productdetails.objects.all()
    print(get_data)
    return render (request,'showdata.html',{'getdata':get_data})

def delete(request,id):
    deleteid = productdetails.objects.get(id=id)
    productdetails.delete(deleteid)
    return redirect ('showdata')