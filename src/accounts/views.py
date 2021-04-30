from django import forms
from django.core.checks.messages import Error
from django.db.models.base import Model
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import FormMixin, FormView

from accounts.decorators import admin_required, doctor_required
from .models import Patient, Doctor, User, Receptionist
from .forms import AccountantRegistrationForm, DoctorRegistrationForm, LabTechnicianRegistrationForm, NurseRegistrationForm, ReceptionistRegistrationForm, UserRegistrationForm, UserEditForm, PatientRegistrationForm
from django.contrib import auth
import sweetify
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Group, User
from django.http import HttpResponse, request
from django.contrib import messages
from django.views.generic import CreateView, View, DetailView, DeleteView
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError
from django.db import transaction
from django.contrib.auth.decorators import login_required


def generate_groups(request):
    groups = ['Doctor', 'Patient', 'Nurse', 'Accountant', 'Receptionist', 'Admin']
    for group_name in groups:
        gp_name = Group.objects.get(name=group_name)
        if gp_name is None:
            new = Group()
            new.name = group_name
            new.save()
            messages.success(request, f'Group "{group_name}" created successfully')
        else:
            messages.warning(request, f'Group "{group_name}" already exists!')
    return HttpResponse(':)')

# class UserRegistrationMixin(FormMixin, View):
#     form_class = UserRegistrationForm
#     template_name = 'accounts/register.html'

#     def get_context_data(self, **kwargs):
#         # self.object = self.get_object()
#         context = super().get_context_data(**kwargs)
#         context['user_form'] = self.form_class
#         return context
    
#     # def render(self, request):
#     #     return self.render_to_response({'user_form':user_form})

#     def get_user_form(self, data=None, files=None, group_name='Patient'):
#         user_form = self.form_class(data, files, group_name)
#         return user_form

#     def get(self, request, *args, **kwargs):
#         return self.render_to_response(self.get_context_data())
    
#     def post(self, request, group_name='Patient', *args, **kwargs):
#         user_form = self.get_user_form(data=request.POST, files=request.FILES, group_name=group_name)
#         if user_form.is_valid():
#             new_user = user_form.save(commit=False)
#             password = user_form.cleaned_data['password']
#             new_user.set_password(password)
#             new_user.save()
#             messages.success(request, f'New user "{new_user}" created!')
#             group, created = Group.objects.get_or_create(group_name)
#             if created:
#                 messages.info(request, f"New group {group} created. Please add it's permissions or contact admin")
#         return self.render_to_response({'user_form':user_form})

# class PatientRegistrationView(UserRegistrationMixin, TemplateResponseMixin):
#     model = Patient
#     profile_form_class = PatientRegistrationForm
#     template_name = 'accounts/register.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['profile_form'] = self.profile_form_class
#         return context

#     def get_patient_form(self, data=None, files=None, model_name='Patient'):
#         profile_form = self.profile_form_class(data, files, model_name)
#         return profile_form

#     def get(self, request, *args, **kwargs):
#         return render(request, self.template_name, self.get_context_data())
    
#     # @transaction.atomic
#     def post(self, request, *args, **kwargs):
#         profile_form = self.get_patient_form(data=request.POST, files=request.FILES, model_name='Patient')
#         if profile_form.is_valid():
#             model_name.objects.create()
#             # profile = profile_form.save(commit=False)
#             # profile.user = new_user
#             # profile.save()
#             messages.success(request, f'Profile for user created!')
#         return render(request, self.template_name, self.get_context_data())

@transaction.atomic
def register_patient(request):
    u_form = UserRegistrationForm(data=request.POST or None, files=request.FILES or None)
    p_form = PatientRegistrationForm(data=request.POST or None, files=request.FILES or None)
    if u_form.is_valid() and p_form.is_valid():
        user = u_form.save(commit=False)
        user.set_password(u_form.cleaned_data['password'])
        user.save()
        profile = p_form.save(commit=False)
        profile.user = user
        profile.user_type = 'patient'
        profile.save()
        group, created = Group.objects.get_or_create(name='Patient')
        if created:
            messages.warning(request, f'New group "{group}" created! Please assign this group permissions.')
        group.user_set.add(user)
        return render(request, 'accounts/register_done.html', {'new_user': user})
    return render(request, 'accounts/register.html', {'user_form': u_form, 'profile_form':p_form, 'register_var':'Patient'})

# @doctor_required
@transaction.atomic
def register_doctor(request):
    u_form = UserRegistrationForm(data=request.POST or None, files=request.FILES or None)
    p_form = DoctorRegistrationForm(data=request.POST or None, files=request.FILES or None)
    if u_form.is_valid() and p_form.is_valid():
        user = u_form.save(commit=False)
        user.set_password(u_form.cleaned_data['password'])
        user.save()
        profile = p_form.save(commit=False)
        profile.user = user
        profile.user_type = 'doctor'
        profile.save()
        group, created = Group.objects.get_or_create(name="Doctor")
        if created:
            messages.warning(request, f'New group "{group}" created! Please assign this group permissions.')
        group.user_set.add(user)
        return render(request, 'accounts/register_done.html', {'new_user': user})
    return render(request, 'accounts/register.html', {'user_form': u_form, 'profile_form':p_form, 'register_var':'Doctor'})

@transaction.atomic
def register_receptionist(request):
    u_form = UserRegistrationForm(data=request.POST or None, files=request.FILES or None)
    p_form = ReceptionistRegistrationForm(data=request.POST or None, files=request.FILES or None)
    if u_form.is_valid() and p_form.is_valid():
        user = u_form.save(commit=False)
        user.set_password(u_form.cleaned_data['password'])
        user.save()
        profile = p_form.save(commit=False)
        profile.user = user
        profile.user_type = 'receptionist'
        profile.save()
        group, created = Group.objects.get_or_create(name="Nurse")
        if created:
            messages.warning(request, f'New group "{group}" created! Please assign this group permissions.')
        group.user_set.add(user)
        return render(request, 'accounts/register_done.html', {'new_user': user})
    return render(request, 'accounts/register.html', {'user_form': u_form, 'profile_form':p_form, 'register_var':'Receptionist'})

@transaction.atomic
def register_nurse(request):
    u_form = UserRegistrationForm(data=request.POST or None, files=request.FILES or None)
    p_form = NurseRegistrationForm(data=request.POST or None, files=request.FILES or None)
    if u_form.is_valid() and p_form.is_valid():
        user = u_form.save(commit=False)
        user.set_password(u_form.cleaned_data['password'])
        user.save()
        profile = p_form.save(commit=False)
        profile.user = user
        profile.user_type = 'nurse'        
        profile.save()
        group, created = Group.objects.get_or_create(name="Nurse")
        if created:
            messages.warning(request, f'New group "{group}" created! Please assign this group permissions.')
        group.user_set.add(user)
        return render(request, 'accounts/register_done.html', {'new_user': user})
    return render(request, 'accounts/register.html', {'user_form': u_form, 'profile_form':p_form, 'register_var':'Nurse'})

@transaction.atomic
def register_accountant(request):
    u_form = UserRegistrationForm(data=request.POST or None, files=request.FILES or None)
    p_form = AccountantRegistrationForm(data=request.POST or None, files=request.FILES or None)
    if u_form.is_valid() and p_form.is_valid():
        user = u_form.save(commit=False)
        user.set_password(u_form.cleaned_data['password'])
        user.save()
        profile = p_form.save(commit=False)
        profile.user = user
        profile.save()
        group, created = Group.objects.get_or_create(name="Accountant")
        if created:
            messages.warning(request, f'New group "{group}" created! Please assign this group permissions.')
        group.user_set.add(user)
        return render(request, 'accounts/register_done.html', {'new_user': user})
    return render(request, 'accounts/register.html', {'user_form': u_form, 'profile_form':p_form, 'register_var':'Accountant'})

@admin_required
@transaction.atomic
def register_labtech(request):
    u_form = UserRegistrationForm(data=request.POST or None, files=request.FILES or None)
    p_form = LabTechnicianRegistrationForm(data=request.POST or None, files=request.FILES or None)
    if u_form.is_valid() and p_form.is_valid():
        user = u_form.save(commit=False)
        user.set_password(u_form.cleaned_data['password'])
        user.save()
        profile = p_form.save(commit=False)
        profile.user = user
        profile.user_type = 'lab_tech'
        profile.save()
        group, created = Group.objects.get_or_create(name="Lab Tech")
        if created:
            messages.warning(request, f'New group "{group}" created! Please assign this group permissions.')
        group.user_set.add(user)
        return render(request, 'accounts/register_done.html', {'new_user': user})
    return render(request, 'accounts/register.html', {'user_form': u_form, 'profile_form':p_form, 'register_var':'Lab Technician'})


def login(request):
    """
    login user
    input: username and password
    """
    # if request.user.is_authenticated:
    #     return redirect("dashboard")
    # else:
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password) # returns none or user object
        if user is not None:
            if user.is_active:
                # user_profile = Patient.objects.get(user=user)
                auth.login(request, user)
                # request.session['user'] = user_profile.user.username
                # request.session['uid'] = user_profile.user.pk
                return redirect('dashboard')
            else:
                return HttpResponse("Disabled account")
        else:
            messages.error(request, 'Invalid credentials')
            sweetify.error(request, 'Invalid credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')

@login_required
def dashboard(request):
    context = {
        'user':"sd"
    }
    return render(request, 'accounts/dashboard.html', context)

def logout(request):
    """
    logout user
    """
    if request.method == 'POST':
        # cache.clear()
        request.session.flush()
        auth.logout(request)
        return render(request, 'accounts/login.html')
    auth.logout(request)
    return render(request, 'accounts/logged_out.html')

@login_required
def edit_patient(request):
    u_form = UserEditForm(instance=request.user, data=request.POST or None, files=request.FILES or None)
    p_form = PatientRegistrationForm(instance=request.user.patient, data=request.POST or None, files=request.FILES or None)
    if u_form.is_valid() and p_form.is_valid():
        u_form.save()
        p_form.save()
        messages.success(request, f"Profile updated successfully!")
    context = {
        'user_form':u_form,
        'profile_form':p_form,
    }
    return render(request, 'accounts/edit.html', context)
