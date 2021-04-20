from django.contrib import admin

from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient', 'receptionist', 'doctor', 'case', 'appointment_time', 'created', 'updated']
    list_filter = ['appointment_time', 'created', 'updated']
    date_hierarchy = "created"
    search_fields = ['patient', 'receptionist', 'doctor', 'case']    
