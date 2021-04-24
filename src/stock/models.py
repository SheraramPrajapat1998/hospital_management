from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.
class Items(models.Model):
    item_name = models.CharField(max_length=50)
    cost_price = models.IntegerField()
    sell_price = models.IntegerField()
    manufacturer = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.item_name


class Stock(models.Model):
    item            = models.ForeignKey(Items, on_delete=models.CASCADE, related_name='stock_item')
    quantity        = models.IntegerField()
    available       = models.BooleanField(default=True)
    purchase_date   = models.DateTimeField(auto_now=True)
    expiry_date     = models.DateField()

    def __str__(self):
        return self.item.item_name