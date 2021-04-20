from django.db import models
from django.conf import settings
from django.urls import reverse
from accounts.models import Patient
from case.models import Case


class Appointment(models.Model):
    patient             = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='appointment_patient')
    receptionist        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='appointment_receptionist')
    doctor              = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='appointment_doctor')
    case                = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='appointment_case')
    appointment_time    = models.DateTimeField()
    created             = models.DateTimeField(auto_now_add=True)
    updated             = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient.username} with {self.doctor.username}, {self.appointment_time}"
        # return f"{self.patient.user.username} with {self.doctor.user.username}, {self.appointment_time}"

    def get_absolute_url(self):
        return reverse('appointment:appointment_detail', kwargs={'pk': self.pk})

    def get_absolute_update_url(self):
        return reverse('appointment:appointment_update', kwargs={'pk': self.pk})

    def get_absolute_delete_url(self):
        return reverse('appointment:appointment_delete', kwargs={'pk': self.pk})