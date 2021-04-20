from django.db import models
from .validators import validate_future_date
from django.conf import settings
from django.contrib.auth.models import AbstractUser, User
from django.core.validators import RegexValidator
from django.urls import reverse

GENDER = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('others', 'Others'),
)

BLOOD_GROUP = (
    ('A+', 'A+'), ('A-', 'A-'),
    ('B+', 'B+'), ('B-', 'B-'),
    ('AB+', 'AB+'), ('AB-', 'AB-'),
    ('O+', 'O+'), ('O-', 'O-'),
)

MARITAL_STATUS = (
    ('single', 'Single'),
    ('married', 'Married'),
    ('widowed', 'Widowed'),
    ('divorced', 'Divorced'),
)

USER_TYPES = (
    ('patient', 'Patient'),
    ('doctor', 'Doctor'),
    ('receptionist', 'Receptionist'),
    ('admin', 'Admin'),
    ('nurse', 'Nurse'),
    ('accountant', 'Accountant'),
)

class User(AbstractUser):
    user_type       = models.CharField(choices=USER_TYPES, default='patient', max_length=20)
    date_of_birth   = models.DateField(blank=True, null=True, validators=[validate_future_date])
    phone_regex     = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+9199999999'. Up to 15 digits allowed.")
    mobile_num      = models.CharField(max_length=15, validators=[phone_regex])
    created         = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)
    date_joining    = models.DateTimeField(auto_now_add=True)
    gender          = models.CharField(default='male', choices=GENDER, max_length=10)
    father_name     = models.CharField(max_length=50)
    mother_name     = models.CharField(blank=True, max_length=50, null=True)
    blood_group     = models.CharField(max_length=5, choices=BLOOD_GROUP, null=True, blank=True)
    marital_status  = models.CharField(max_length=10, choices=MARITAL_STATUS, default='single')
    photo           = models.ImageField(default="default.png", upload_to="patients/%Y/%m/%d", blank=True)
    # aadhar_number = models.BigIntegerField(verbose_name='Aadhar Number')
    address1        = models.CharField(max_length=100)
    address2        = models.CharField(max_length=100, blank=True)
    city            = models.CharField(max_length=50)
    zipcode         = models.BigIntegerField(default=0)
    state           = models.CharField(max_length=20)
    # country   = models.CharField(max_length=20)
    
    @property
    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}({self.username})"


class Staff(models.Model):
    aadhar_number   = models.BigIntegerField(verbose_name='Aadhar Number')
    empCategory     = models.CharField(max_length=20, blank=True, verbose_name='Employee Category')

    class Meta:
        abstract = True

class Patient(models.Model):
    user                = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_discharge   = models.DateTimeField(auto_now=True)
    allergies           = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}({self.user.username})"

    # def get_absolute_url(self):
    #     return reverse('account:user', kwargs={'pk': self.pk})


class Doctor(models.Model):
    DEPARTMENTS = [('Cardiologist', 'Cardiologist'),
                    ('Dermatologists', 'Dermatologists'),
                    ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'),
                    ('Allergists/Immunologists', 'Allergists/Immunologists'),
                    ('Anesthesiologists', 'Anesthesiologists'),
                    ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons')
                ]
    user        = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)    
    languages   = models.CharField(max_length=20)
    speciality  = models.CharField(max_length=20)
    department  = models.CharField(max_length=50, choices=DEPARTMENTS)    
    # patients    = models.ManyToManyField(Patient, related_name='doctors')

    # def get_absolute_url(self):
    #     return reverse('account:user', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}({self.user.username})"
    

class Receptionist(Staff):
    user    = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # patient = models.ManyToManyField(Patient, related_name='receptionists', blank=True)
    
    def __str__(self):
        return f"{self.user.first_name}"

class Nurse(Staff):
    user  = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'Nurses'

class Accountant(Staff):
    user  = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    



# class StaffDocuments(models.Model):
#     """ Employee Document Table"""
#     employee = models.OneToOneField(
#         Staff, primary_key=True, on_delete=models.CASCADE, blank=True)
#     photo = models.FileField(upload_to=user_directory_path, blank=True)
#     qualificationDoc = models.FileField(
#         upload_to=user_directory_path, blank=True)
#     IdProof = models.FileField(upload_to=user_directory_path, blank=True)
#     addressProof = models.FileField(upload_to=user_directory_path, blank=True)
#     otherDoc = models.FileField(upload_to=user_directory_path, blank=True)

#     def __str__(self):
#         return f"Name:{self.employee.fullName}"

#     def save(self, *args, **kwargs):
#         super(EmployeeDocuments, self).save(*args, **kwargs)

#         # compress only if IMG file
#         try:
#             img = Image.open(self.image.path)  # Open image using self

#             if img.height > 400 or img.width > 400:
#                 new_img = (400, 400)
#                 img.thumbnail(new_img)
#                 img.save(self.image.path)

#         # else ingore
#         except:
#             pass

# def user_directory_path(instance, filename):
#     """file will be uploaded to given path"""
#     return 'staff/{0}/{1}'.format(instance.employee.empID, filename)

# class Profile(models.Model):
#     "User Table"
#     USER_TYPE = (
#         ('patient', 'Patient'),
#         ('doctor', 'Doctor'),
#         ('nurse', 'Nurse'),
#         ('receptionist', 'Receptionist'),
#         ('admin', 'Admin'),        
#     )
#     user            = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     full_name       = models.CharField(max_length=50, default="")
#     user_type       = models.CharField(max_length=20, choices=USER_TYPE, default="patient")
#     date_of_birth   = models.DateField(null=True, blank=True)

#     def __str__(self):
#         return f"{self.user}"


