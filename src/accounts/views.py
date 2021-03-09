from django import forms
from django.core.checks.messages import Error
from django.db.models.base import Model
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import FormView
from .models import Patient, Doctor, User, Receptionist
from .forms import AccountantRegistrationForm, DoctorRegistrationForm, NurseRegistrationForm, ReceptionistRegistrationForm, UserRegistrationForm, UserEditForm, PatientRegistrationForm
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

# def register(request, profile_form=None, user_type='patient', model_name=Patient, template_name=None):
#     u_form = UserRegistrationForm(data=request.POST or None)
#     profile_form = profile_form(data=request.POST or None, files=request.FILES or None)
#     if u_form.is_valid() and profile_form.is_valid():
#         new_user = u_form.save(commit=False)
#         new_user.set_password(u_form.cleaned_data['password'])
#         # new_user.user_type = user_type
#         new_user.save()
#         profile = profile_form(commit=False)
#         profile.user = new_user
#         profile.save()
#         g, created = Group.objects.get_or_create(name=str(model_name)) 
#         if created:
#             messages.warning(f"New group '{g}' created! Please add it's permissions.")
#             print('group created...')
#         g.user_set.add(new_user)
#         return render(request, 'accounts/register_done.html', {'new_user': new_user})
#     return render(request, 'accounts/register.html', {'user_form': u_form, 'profile_form':profile_form})
 
# def register_patient(request):
#     return register(request, profile_form=PatientRegistrationForm, model_name=Patient, user_type='patient')

# def register_doctor(request):
#     return register(request, profile_form=DoctorRegistrationForm, model_name=Doctor, user_type='doctor')

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
        profile.save()
        group, created = Group.objects.get_or_create(name='Patient')
        if created:
            messages.warning(request, f'New group "{group}" created! Please assign this group permissions.')
        group.user_set.add(user)
        return render(request, 'accounts/register_done.html', {'new_user': user})
    return render(request, 'accounts/register.html', {'user_form': u_form, 'profile_form':p_form})


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
        profile.save()
        group, created = Group.objects.get_or_create(name="Doctor")
        if created:
            messages.warning(request, f'New group "{group}" created! Please assign this group permissions.')
        group.user_set.add(user)
        return render(request, 'accounts/register_done.html', {'new_user': user})
    return render(request, 'accounts/register.html', {'user_form': u_form, 'profile_form':p_form})

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
        profile.save()
        group, created = Group.objects.get_or_create(name="Doctor")
        if created:
            messages.warning(request, f'New group "{group}" created! Please assign this group permissions.')
        group.user_set.add(user)
        return render(request, 'accounts/register_done.html', {'new_user': user})
    return render(request, 'accounts/register.html', {'user_form': u_form, 'profile_form':p_form})

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
        profile.save()
        group, created = Group.objects.get_or_create(name="Nurse")
        if created:
            messages.warning(request, f'New group "{group}" created! Please assign this group permissions.')
        group.user_set.add(user)
        return render(request, 'accounts/register_done.html', {'new_user': user})
    return render(request, 'accounts/register.html', {'user_form': u_form, 'profile_form':p_form})

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
        profile.save()
        group, created = Group.objects.get_or_create(name="Nurse")
        if created:
            messages.warning(request, f'New group "{group}" created! Please assign this group permissions.')
        group.user_set.add(user)
        return render(request, 'accounts/register_done.html', {'new_user': user})
    return render(request, 'accounts/register.html', {'user_form': u_form, 'profile_form':p_form})

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
    return render(request, 'accounts/register.html', {'user_form': u_form, 'profile_form':p_form})


def login(request):
    """
    login user
    input: username and password
    """
    if request.user.is_authenticated:
        return redirect("dashboard")
    else:
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
