from django.urls import path

from .import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.CreateBillView.as_view(), name='bill_create'),
]