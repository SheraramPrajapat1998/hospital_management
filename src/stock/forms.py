from django import forms
from .models import Stock, Items
from django.forms.models import inlineformset_factory

# class StockForm (forms.ModelForm):
#     class Meta:
#         model = Stock
#         fields = ['item', 'quantity', 'available', 'purchase_date', 'expiry_date']

# class ItemsForm(forms.ModelForm):
#     class Meta:
#         model = Items
#         fields = ['item_name', 'cost_price', 'sell_price', 'manufacturer', 'description', 'quantity']

ItemsFormSet = inlineformset_factory(Stock, Items, fields=['item_name', 'cost_price', 'sell_price', 'manufacturer', 'description', 'quantity'], extra=2, can_delete=True)