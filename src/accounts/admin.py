from django.contrib import admin
from django.contrib.auth.models import User

from .models import Accountant, Doctor, Nurse, Patient, Receptionist
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(Patient)
admin.site.register(Doctor)
# admin.site.register(Accountant)
# admin.site.register(Nurse)
# admin.site.register(Receptionist)
admin.site.register(User, UserAdmin)

# @admin.register(Patient)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ['user', 'date_of_birth', 'mobile_num', 'created', 'updated']
#     list_filter = [ 'created', 'updated']
#     search_fields  = ['user', 'mobile_num']
#     date_hierarchy = "created"
