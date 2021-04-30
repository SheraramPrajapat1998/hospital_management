from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.

class Stock(models.Model):
    name            = models.CharField(max_length=255)
    description     = models.TextField(null=False, blank=False)
    # quantity        = models.IntegerField()
    available       = models.BooleanField(default=True)
    purchase_date   = models.DateTimeField(auto_now=True)
    expiry_date     = models.DateField()
    created         = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.description}[:10] -Exp. Date: {self.expiry_date} "

    def get_absolute_url(self):
        return reverse('stock:stock_detail', kwargs={'pk': self.pk})

    def get_absolute_update_url(self):
        return reverse('stock:stock_update', kwargs={'pk': self.pk})

    def get_absolute_delete_url(self):
        return reverse('stock:stock_delete', kwargs={'pk': self.pk})

    def get_total_items(self):
        total_items = sum(item.get_quantity() for item in self.items.all())
        return total_items


class Items(models.Model):
    stock = models.ForeignKey(Stock, related_name='items', on_delete=models.CASCADE)
    item_name = models.CharField(max_length=50)
    cost_price = models.IntegerField()
    sell_price = models.IntegerField()
    manufacturer = models.CharField(max_length=50)
    description = models.TextField()
    quantity    = models.IntegerField(default=1)
    
    def __str__(self):
        return self.item_name

    def get_quantity(self):
        total_items = self.quantity
        return total_items