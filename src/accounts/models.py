from django.db import models

from django.conf import settings


class Profile(models.Model):
    "User Table"
    USER_TYPE = (
        ('patient', 'P'),
        ('doctor', 'D'),
        ('nurse', 'N'),
        ('admin', 'A'),        
    )
    user            = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name       = models.CharField(max_length=50, default="")
    user_type       = models.CharField(max_length=20, choices=USER_TYPE, default="patient")
    date_of_birth   = models.DateField(null=True, blank=True)
    mobile_num      = models.BigIntegerField(default=0)
    photo           = models.ImageField(default="default.png", upload_to="users/%Y/%m/%d", blank=True)
    created         = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.user}"


