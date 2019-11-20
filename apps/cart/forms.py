from django import forms

from .models import Item


class CartItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = 'quantity'
