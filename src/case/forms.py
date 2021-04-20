from django import forms
from .models import Case

class CaseForm(forms.ModelForm):
    filed_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    closed_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=False)

    class Meta:
        model = Case
        fields = ['patient', 'receptionist', 'description', 'filed_date', 'closed_date', 'status']
