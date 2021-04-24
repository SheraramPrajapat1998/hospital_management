from django.conf import settings
from django.db import models
from django.urls import reverse

class Case(models.Model):
    STATUS_CHOICES = (
        ('open', 'OPEN'),
        ('closed', 'CLOSED'),
    )
    patient         = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cases')
    receptionist    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='case_receptionist')
    description     = models.TextField()
    filed_date      = models.DateTimeField()
    closed_date     = models.DateTimeField(default=None, blank=True, null=True)
    status          = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open') # status of case CLOSE/OPEN

    def __str__(self):
        return f"Patient: {self.patient.username} - Desc:{self.description[:20]}"
    
    def get_absolute_url(self):
        return reverse('case:case_detail', kwargs={'pk': self.pk})