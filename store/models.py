from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,blank=True)
    name = models.CharField(null=True, max_length=200)
    email=models.EmailField(null=True,max_length=254)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(null=True, max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False,null=True,blank=False)
    image=models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name

    @property
    def imageUrl(self):
        try:
            url=self.image.url
        except:
            url=''
        return url

class Order(models.Model):
    customer = models.ForeignKey(Customer,null=True,blank=True,on_delete=models.SET_NULL)
    dateOrdered = models.DateTimeField(auto_now_add=True)
    complete  = models.BooleanField(default=False,null=True,blank=False)
    tranctionId=models.CharField(null=True, max_length=200)
    
    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product=models.ForeignKey(Product,null=True,blank=True,on_delete=models.SET_NULL)
    order=models.ForeignKey(Order,null=True,blank=True,on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=0, null=True,blank=True)
    dateAdded = models.DateTimeField(auto_now_add=False)

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,null=True,blank=True,on_delete=models.SET_NULL)
    order=models.ForeignKey(Order,null=True,blank=True,on_delete=models.SET_NULL)
    address=models.CharField( max_length=200)
    city=models.CharField( max_length=200)
    state=models.CharField( max_length=200)
    zipcode=models.IntegerField()
    dateAdded=models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.address
    