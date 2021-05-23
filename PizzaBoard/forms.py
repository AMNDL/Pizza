from django import forms
from PizzaBoard.models import Order
import datetime


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('price',)
    
    def clean(self):
        super(OrderForm, self).clean()
