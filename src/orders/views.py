from django.forms import fields
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormMixin

from orders.forms import BillCreateForm
from orders.models import Bill, BillItem

class CommonOrderMixin(LoginRequiredMixin, PermissionRequiredMixin):
    permission_denied_message = "You are not authorized to this page!"
    permission_required = 'orders.view_bill'
    model = Bill

class OrderFormMixin(CommonOrderMixin):
    form = BillCreateForm
    # form = BillItemFormSet
    fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'paid']
    # fields = ['quantity']
class CreateBillView(OrderFormMixin, CreateView):
    permission_required = 'orders.add_bill'
    template_name = 'orders/bill_form.html'


class BillListView(CommonOrderMixin, ListView):
    template_name = 'orders/bill_list.html'
    context_object_name = 'bills'


# def create_bill(request):
#     bill_form = BillCreateForm(data=request.POST or None)
#     billItem_form = BillItemFormSet(data=request.POST or None)
#     if request.method == request.POST:
#         bill = bill_form.save(commit=False)
#         bill.