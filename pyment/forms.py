from django import forms
from .models import BillingAdress
from cart.models import Order

class BillingAdressForm(forms.ModelForm):
    class Meta:
        model = BillingAdress
        fields = '__all__'
        exclude = ('user',)

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['payment_method']
