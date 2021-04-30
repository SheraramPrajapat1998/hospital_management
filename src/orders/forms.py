from django import forms
from django.forms.models import inlineformset_factory
from .models import Bill, BillItem

class BillCreateForm(forms.ModelForm):
    first_name  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First name...'}))
    last_name   = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last name...'}))
    email       = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email...'}))
    address     = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Address...'}))
    postal_code = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Postal Code...'}))
    city        = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'City...'}))
    # postal_code = INZipCodeField()
    postal_code = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Postal Code...'}))
    
    class Meta:
        model = Bill
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']


# BillItemFormSet = inlineformset_factory(Bill, BillItem, fields=['name', 'quantity'], can_delete=True, extra=2)