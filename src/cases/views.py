from django.shortcuts import render

from .models import Case
from .forms import CaseForm

def generate_case(request):
    form = CaseForm()
    if request.method == 'POST':
        form = CaseForm(data=request.POST)
        if form.is_valid():
            form.save()
            