from django import forms
from django.forms import widgets
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    # appointment_time = forms.DateField(widget=forms.widgets.DateTimeInput(format='%d/%m/%Y %H:%M', attrs={'type': 'time'}), required=True)

    class Meta:
        model = Appointment
        fields = ['patient', 'receptionist', 'doctor', 'case', 'appointment_time']
        