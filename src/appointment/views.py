from django.http.response import Http404
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from .models import Appointment
from .forms import AppointmentForm
from django.contrib import messages
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy

class CommonAppointmentMixin(LoginRequiredMixin, PermissionRequiredMixin):
    model = Appointment

class AppointmentFormMixin(CommonAppointmentMixin):
    form_class = AppointmentForm
    template_name = "appointment/form.html"

class AppointmentCreateView(AppointmentFormMixin, CreateView):
    permission_required = "appointment.add_appointment"

class AppointmentListView(CommonAppointmentMixin, ListView):
    template_name = "appointment/list.html"
    context_object_name = "appointments"
    permission_required = "appointment.view_appointment"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        appointments = Appointment.objects.all()
        # print(self.request.user.user_type)
        # if self.request.user.user_type == 'patient':
        #     appointments = appointments.filter(patient=self.request.user)
        # elif self.request.user.user_type == 'doctor':
        #     appointments = appointments.filter(doctor = self.request.user)
        # elif self.request.user.user_type == 'receptionist':
        #     appointments = appointments.filter(receptionist = self.request.user)
        context['appointments'] = appointments
        return context

class AppointmentDetailView(CommonAppointmentMixin, DetailView):
    template_name = "appointment/detail.html"
    permission_required = "appointment.view_appointment"

class AppointmentUpdateView(AppointmentFormMixin, UpdateView):
    permission_required = "appointment.change_appointment"

class AppointmentDeleteView(CommonAppointmentMixin, DeleteView):
    template_name = "appointment/delete_confirm.html"
    permission_required = "appointment.delete_appointment"
    success_url = reverse_lazy("appointment:appointment_list")
    