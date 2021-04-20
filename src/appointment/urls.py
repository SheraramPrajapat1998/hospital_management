from django.urls import path
from .import views

app_name = "appointment"

urlpatterns = [
    path('', views.AppointmentListView.as_view(), name="appointment_list"),
    path('<int:pk>/', views.AppointmentDetailView.as_view(), name="appointment_detail"),
    path('create/', views.AppointmentCreateView.as_view(), name="appointment_create"),
    path('<int:pk>/update/', views.AppointmentUpdateView.as_view(), name="appointment_update"),
    path('<int:pk>/delete/', views.AppointmentDeleteView.as_view(), name="appointment_delete"),
]