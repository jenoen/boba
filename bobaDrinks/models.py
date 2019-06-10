from django.db import models
from django.urls import reverse

class Customer(models.Model):
    customerName = models.CharField(max_length=64)
    #time = models.DateTimeField(auto_now=False, auto_now_add=True)

    drinks = models.ManyToManyField('Drink')
    


class Drink(models.Model):
    topping = models.CharField(max_length=100, choices=[
        ("BOBA", 'boba'),
        ("JELLY", 'jelly'),
        ("LYCHEE", 'lychee'),
        ("REDBEAN", 'redbean'),
        ("AGAR", 'agar'),        
    ])
    ice = models.BooleanField(null=True)
    drinkBase = models.CharField(max_length=100, choices=[
        ("GREEN", 'green'),
        ("BLACK", 'black'),
        ("MILK", 'milk'),
        ("TARO", 'taro'),
        ("THAI", 'thai'),      
    ])
    sugarLevel = models.CharField(max_length=100, choices=[
        ("0%", '0%'),
        ("25%", '25%'),
        ("50%", '50%'),
        ("75%", '75%'),
        ("100%", '100%'),        
    ])
