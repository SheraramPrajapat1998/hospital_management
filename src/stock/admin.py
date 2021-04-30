from django.contrib import admin

from .models import Stock, Items

class ItemsInline(admin.TabularInline):
    model = Items

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['id', 'available', 'purchase_date', 'expiry_date', 'created', 'updated']
    inlines = [ItemsInline]

