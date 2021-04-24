from django.urls import path
from .import views

app_name = "report"

urlpatterns = [
    path('', views.ReportListView.as_view(), name='report_list'),
    path('<int:id>/', views.ReportDetailView.as_view(), name='report_detail'),
    path('create/', views.ReportCreateView.as_view(), name='report_create'),
    path('<int:id>/delete/', views.ReportDeleteView.as_view(), name='report_delete'),
]
