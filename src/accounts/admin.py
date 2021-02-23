from django.contrib import admin

from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'user_type', 'date_of_birth', 'mobile_num', 'created', 'updated']
    list_filter = ['user_type', 'created', 'updated']
    search_fields  = ['user', 'full_name', 'user_type', 'mobile_num']
    date_hierarchy = "created"