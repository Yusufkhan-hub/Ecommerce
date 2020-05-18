from django.shortcuts import render
from .models import *
# Create your views here.
def store(request):
    if request.method=="GET":
        product=Product.objects.all()
        context={'product':product}
        return render(request,'store/Store.html',context)

def cart(request):
    if request.method=="GET":
        context={}
        return render(request,'store/Cart.html',context)

def checkout(request):
    if request.method=="GET":
        context={}
        return render(request,'store/Checkout.html',context)
 