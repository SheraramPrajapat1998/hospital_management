from django import forms
# from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model
from django.forms import fields
from .models import Accountant, Nurse, Patient, Doctor, User, Receptionist


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
    email = forms.EmailField(label='Email')
    date_of_birth = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    class Meta:
        # gives current active model either Custom User or default User model
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email',
                  'date_of_birth', 'photo', 'mobile_num', 'gender',
                  'father_name', 'mother_name', 'blood_group', 'marital_status',
                  'address1', 'address2', 'city', 'zipcode', 'state'
                  ]
        exclude = ['groups', 'superuser_status',
                   'is_staff', 'is_superuser', ]

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match")
        return cd['password2']


class PatientRegistrationForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['allergies']
        exclude = ['user', ]


class DoctorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['languages', 'speciality', 'department']
        exclude = ['user', 'patient']


class ReceptionistRegistrationForm(forms.ModelForm):
    class Meta:
        model = Receptionist
        fields = []
        exclude = ['user', 'patient']

class NurseRegistrationForm(forms.ModelForm):
    class Meta:
        model = Nurse
        fields = []
        exclude = ['user', ]

class AccountantRegistrationForm(forms.ModelForm):
    class Meta:
        model = Accountant
        fields = []
        exclude = ['user', ]


class UserEditForm(forms.ModelForm):
    email = forms.EmailField(label='Email')
    date_of_birth = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',
                  'date_of_birth', 'photo', 'mobile_num', 'gender',
                  'father_name', 'mother_name', 'blood_group', 'marital_status',
                  'address1', 'address2', 'city', 'zipcode', 'state'
                  ]