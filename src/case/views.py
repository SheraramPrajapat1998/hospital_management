from os import close
from django.http import request
from django.http.response import Http404
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from .models import Case
from .forms import CaseForm
from django.contrib import messages
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy

@login_required
def generate_case(request):
    case_form = CaseForm(data=request.POST or None)
    if case_form.is_valid():
        case_form.save()
        # items
        # bill
        messages.success(request, f'Case generated successfully!')
        return render(request, 'case/generate.html', {'case_form':case_form})
    context = {'case_form':case_form}
    return render(request, 'case/generate.html', context)

class CommonMixin(LoginRequiredMixin, PermissionRequiredMixin):
    model = Case

class CaseFormMixin(CommonMixin):
    form_class = CaseForm
    template_name = 'case/form.html'
    
class CaseListView(CommonMixin, ListView):
    template_name = 'case/case_list.html'
    context_object_name = 'cases'

    # def get_queryset(self):
    #     return super().get_queryset() 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cases = Case.objects.all()
        # open_cases = cases.filter(closed_date!=None)
        # closed_cases = cases.filter(closed_date=None)
        # print(closed_cases)

        if self.request.user.user_type == 'patient':
            cases = cases.filter(patient=self.request.user)
        # context['openCases'] = Case.objects.filter(closed_date)
        # context['closed_cases'] = closed_cases
        else: 
            cases = cases
        return context


class CaseDetailView(CommonMixin, DetailView):
    template_name = 'case/case_detail.html'

class CaseCreateView(CaseFormMixin, CreateView):
    # template_name = 'case/case_create.html'
    permission_required = 'case.add_case'
    # form_class = CaseForm

    # def get(self, request, *args, **kwargs):

    #     return super().get(request, *args, **kwargs)

class CaseUpdateView(CaseFormMixin, UpdateView):
    template_name = 'case/case_update.html'
    permission_required = 'case.change_case'
    
class CaseDeleteView(CommonMixin, DeleteView):
    template_name = 'case/case_delete_confirm.html'
    success_url = reverse_lazy('case:case_list')
    permission_required = "case.delete_case"
    # set permissions 
    # def get_object(self, queryset=None):
    #     obj = super().get_object(queryset=queryset)
    #     if not obj.owner.user_type == 'patient':
    #         raise Http404
    #     return obj
    
