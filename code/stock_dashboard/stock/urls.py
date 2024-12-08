from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dataset_exploration/', views.dataset_explore, name='dataset_explore'),
    path('visualize/<str:stock_name>/', views.visualize_stock, name='visualize_stock'),
]
