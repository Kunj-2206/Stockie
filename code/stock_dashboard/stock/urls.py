from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dataset_exploration/', views.dataset_explore, name='dataset_explore'),
    path('visualize/<str:stock_name>/', views.visualize_stock, name='visualize_stock'),
    path('dashboard/', views.dashboard_view, name='dashboard'),  # Dashboard page
    path('risk/', views.risk_view, name='risk'),  # Risk page
    path('home/', views.home_view, name='home'),  # Dashboard page


]
