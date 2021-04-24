from django.shortcuts import render
from django.http.response import Http404
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from .models import Report
from django.contrib import messages
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy


class CommonReportMixin(LoginRequiredMixin, PermissionRequiredMixin):
    model = Report
    permission_required = "report.view_report"

class ReportListView(CommonReportMixin, ListView):
    template_name = "report/list.html"
    context_object_name = "reports"

class ReportDetailView(CommonReportMixin, DetailView):
    template_name = "report/detail.html"
    permission_required = "report.view_report"

class ReportCreateView(CommonReportMixin, CreateView):
    template_name = "report/create.html"


class ReportUpdateView(CommonReportMixin, UpdateView):
    template_name = ""


class ReportDeleteView(CommonReportMixin, DeleteView):
    template_name = "report/delete_confirm.html"
    permission_required = "report.delete_report"
    success_url = "report:report_list"