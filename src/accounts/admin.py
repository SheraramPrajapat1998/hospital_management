from django.contrib import admin
from django.contrib.auth.models import User

from .forms import CustomUserChangeForm, CustomUserCreationForm

from .models import Accountant, Doctor, LabTechnician, Nurse, Patient, Receptionist
from django.contrib.auth.admin import UserAdmin
from .models import User

#Customize admin site text
admin.site.site_header = "Hospital Management Administration"
admin.site.site_title = "Hospital Management Admin Portal"
admin.site.index_title = "Welcome to Hospital Management Portal"


admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Accountant)
admin.site.register(Nurse)
admin.site.register(Receptionist)
admin.site.register(LabTechnician)
# admin.site.register(User, UserAdmin)
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    date_hierarchy = "created"
    fieldsets = (
        (None, {'fields': ('username', 'user_type', 'password', 'first_name', 'last_name', 'email',
                  'date_of_birth', 'photo', 'mobile_num', 'gender',
                  'father_name', 'mother_name', 'blood_group', 'marital_status',
                  'address1', 'address2', 'city', 'zipcode', 'state', 'last_login', 'date_joined' )}),
        ('Permissions', {'fields': ( 'is_active', 'is_staff', 'is_superuser')}),
        ('Groups and User Permissions', {
            'classes': ('collapse',),
            'fields': ('groups', 'user_permissions'),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', 'extrapretty'),
            'fields': ('username', 'user_type', 'password', 'first_name', 'last_name', 'email',
                  'date_of_birth', 'photo', 'mobile_num', 'gender',
                  'father_name', 'mother_name', 'blood_group', 'marital_status',
                  'address1', 'address2', 'city', 'zipcode', 'state', 'last_login', 'date_joined' )}
        ),
        ('Permissions', {'fields': ( 'is_active', 'is_staff', 'is_superuser')}),
        ('Groups and User Permissions', {
            'classes': ('collapse',),
            'fields': ('groups', 'user_permissions'),
        }),
    )
    radio_fields = {"gender": admin.VERTICAL}

# @admin.register(Patient)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ['user', 'date_of_birth', 'mobile_num', 'created', 'updated']
#     list_filter = [ 'created', 'updated']
#     search_fields  = ['user', 'mobile_num']
#     date_hierarchy = "created"
