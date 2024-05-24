from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    bio = models.TextField(default="no bio...", max_length=300)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=254 , null=True)
    dob = models.DateField(max_length=8, null=True)
    city = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=100,null=True)
    profile_pic = models.ImageField(default="guest-user.jpg", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    
    
    def __str__(self):
        return self.name

class Item(models.Model):
    CATEGORY = (
        ('Indoor' , 'Indoor'),
        ('Out Door' , 'Out Door'),
    )

    name = models.CharField(max_length=50, null=True)
    price = models.FloatField(null=True)
    amount = models.IntegerField(null=True)
    type = models.CharField(max_length=200, null=True, choices=CATEGORY)
    image = models.ImageField(default="protin.jpg", blank=True, null=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name
    

class Order(models.Model):
    STATUS = (
        ('Pending' , 'Pending'),
        ('Out of delivery' , 'Out of delivery'),
        ('Delivered' , 'Delivered'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    item = models.ForeignKey(Item, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=1000, null=True)
    
    def __str__(self):
        return self.item.name