from django.db import models

# Create your models here.

class ContactDb(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Messages = models.CharField(max_length=400,null=True,blank=True)

class UserDB(models.Model):
    Username = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=200,null=True,blank=True)
    Password = models.CharField(max_length=100,null=True,blank=True)

class CartDB(models.Model):
    Username = models.CharField(max_length=100,null=True,blank=True)
    Product = models.CharField(max_length=100,null=True,blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    Total_Price = models.IntegerField(null=True,blank=True)

class UserBillingDB(models.Model):
    Username = models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField(max_length=100,null=True,blank=True)
    Phone = models.IntegerField(null=True,blank=True)
    Address = models.CharField(max_length=200,null=True,blank=True)
    State = models.CharField(max_length=100,null=True,blank=True)
    City = models.CharField(max_length=100,null=True,blank=True)
    Postalcode = models.IntegerField(null=True,blank=True)
    Messages = models.CharField(max_length=100,null=True,blank=True)
    Totalprice = models.IntegerField(null=True,blank=True)


