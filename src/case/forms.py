from django import forms
from .models import Case

class CaseForm(forms.ModelForm):
    filed_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    closed_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}), required=False)

    class Meta:
        model = Case
        fields = ['patient', 'receptionist', 'description', 'filed_date', 'closed_date', 'status']
    
    # def __init__(self, *args, **kwargs):
    #     from django.forms.widgets import HiddenInput
    #     if self.request.user_type == 'receptionist':
    #         hide_condition = kwargs.pop('receptionist', None)
    #     super().__init__(*args, **kwargs)
    #     if hide_condition:
    #         self.fields['fieldname'].widget= HiddenInput()
