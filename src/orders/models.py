from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

from accounts.models import Patient
from stock.models import Items

class Bill(models.Model):
    user        = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='bills')
    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    email       = models.EmailField()
    address     = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city        = models.CharField(max_length=100)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    paid        = models.BooleanField(default=False)
    # country     = CountryField()

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return f"Bill {self.id} user -- {self.first_name} {self.last_name}"

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost


class BillItem(models.Model):
    bill    = models.ForeignKey(Bill, related_name='bill_items', on_delete=models.CASCADE)
    item    = models.ForeignKey(Items, related_name='billitem_items', on_delete=models.CASCADE)
    
    def __str__(self):
        return "{self.id}"

    def get_cost(self):
        return self.item.sell_price * self.item.quantity