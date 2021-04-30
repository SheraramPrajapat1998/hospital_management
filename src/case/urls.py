from django.urls import path

from .import views

app_name = 'case'

urlpatterns = [
    path('generate/', views.generate_case, name='generate_case'),
    path('list/', views.CaseListView.as_view(), name='case_list'),
    path('<int:pk>/', views.CaseDetailView.as_view(), name='case_detail'),
    path('create/', views.CaseCreateView.as_view(), name='case_create'),
    path('<int:pk>/update/', views.CaseUpdateView.as_view(), name='case_update'),
    path('<int:pk>/delete/', views.CaseDeleteView.as_view(), name='case_delete'),
]