from django import forms
from django.db import models
from django.forms import formsets
from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, View, DetailView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import FormMixin
from django.views.generic import ListView
from stock.models import Stock
from .forms import ItemsFormSet
from django.utils import timezone

# Create your views here.

class CommonStockMixin(LoginRequiredMixin, PermissionRequiredMixin):
    model = Stock
    permission_required = "stock.view_stock"
    permission_denied_message = "You are not authorized on this page."
    

class StockListView(CommonStockMixin, ListView):
    template_name = 'stock/list.html'
    context_object_name = 'stocks'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs

class StockDetailView(CommonStockMixin, DetailView):
    template_name = 'stock/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['items'] = self.get_object
        context['today'] = timezone.now()
        return context

# class StockCreateView(CreateView):
#     form = 

class StockItemsUpdateView(TemplateResponseMixin, PermissionRequiredMixin, View):
    template_name = 'stock/formset.html'
    permission_required = 'stock.change_stock'
    stock = None

    def get_formset(self, data=None):
        return ItemsFormSet(instance=self.stock, data=data)
    
    def dispatch(self, request, pk):
        self.stock = get_object_or_404(Stock, id=pk)
        return super().dispatch(request, pk)

    def get(self, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({'stock':self.stock, 'formset':formset})
    
    def post(self, *args, **kwargs):
        formset = self.get_formset(data=self.request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('stock:stock_list')
        return self.render_to_response({'stock':self.stock, 'formset': formset})

class StockDeleteView(CommonStockMixin, DeleteView):
    permission_required = 'stock.delete_stock'
