from django.urls import path

from .import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    # path('dashboard/', views.dashboard, name='dashboard'),

    # path('login/', auth_views.LoginView.as_view(), name='login'),     #built in auth views :templates -> registration folder
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('register/', views.PatientRegistrationView.as_view(), name='register'),

    path('', views.dashboard, name='dashboard'),
    path('patient/register/', views.register_patient, name='register'),
    # path('patient/register/', views.PatientRegistrationView.as_view(), name='patient_register'),
    # path('patient/register/', views.PatientRegistrationView.as_view(), name='patient_register'),
    path('patient/register/', views.register_patient, name='patient_register'),
    path('doctor/register/', views.register_doctor, name='doctor_register'),
    path('nurse/register/', views.register_nurse, name='nurse_register'),
    path('receptionist/register/', views.register_receptionist, name='receptionist_register'),
    path('accountant/register/', views.register_accountant, name='accountant_register'),
    path('lab_technician/register/', views.register_labtech, name='lab_technician_register'),
    path('generate/groups/', views.generate_groups, name='generate_groups'),
    # path('edit/',views.edit, name='edit'),
    path('patient/edit/',views.edit_patient, name='patient_edit'),

    # change password urls
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # reset password urls
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
