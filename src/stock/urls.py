from django.urls import path
from django.views.generic.detail import DetailView

from .import views

app_name = "stock"

urlpatterns = [
    path('', views.StockListView.as_view(), name='stock_list'),
    path('<int:pk>/detail/', views.StockDetailView.as_view(), name='stock_detail'),
    path('create/', views.StockItemsUpdateView.as_view(), name='stock_create'),
    path('<int:pk>/update', views.StockItemsUpdateView.as_view(), name='stock_update'),
    path('<int:pk>/delete', views.StockDeleteView.as_view(), name='stock_delete'),
]