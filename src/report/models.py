from django.db import models
from django.conf import settings
from case.models import Case
from django.urls import reverse

# Create your models here.
class Report(models.Model):
    case            = models.ForeignKey(Case, on_delete=models.CASCADE, related_name="report_case")
    lab_attendant   = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="report_lab_attendant")
    generated_date  = models.DateField(auto_now=True)
    description     = models.TextField()
    created         = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Patient {self.case.patient}'s Report"
    
    def get_absolute_url(self):
        return reverse('report:report_detail', kwargs={'pk': self.pk})
