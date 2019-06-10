from django import forms

from .models import Customer, Drink

class DrinkForm(forms.ModelForm):

    class Meta:
        model = Drink
        fields = ('topping', 'ice', 'drinkBase','sugarLevel',)

class CustomerForm(forms.ModelForm):
      class Meta:
        model = Customer
        fields = ('customerName',)
