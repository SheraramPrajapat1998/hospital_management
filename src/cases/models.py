from django.db import models
from django.contrib.auth.models import User

class Case(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cases')
    receptionist = models.ForeignKey(User, on_delete=models.CASCADE, related_name='case_receptionist')
    description = models.TextField()
    filed_date = models.DateField(auto_now_add=True)
    closed_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.username} - {self.description[:20]}"
    