from django.contrib import admin

from .models import Case

@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ['patient', 'receptionist', 'filed_date', 'closed_date']
    list_filter = ['filed_date', 'closed_date']
    date_hierarchy = "filed_date"
    search_fields = ['patient', 'receptionist', ]