from django.urls import path
from . import views

app_name = 'restaurant'

urlpatterns = [
    path('', views.home, name='restaurant-home'),
    path('menu/', views.menu, name='restaurant-menu'),
    path('uploadDishes/', views.uploadDishes, name='restaurant-uploadDishes'),
    path('uploadCustomers/', views.uploadCustomers, name='restaurant-uploadCustomers'),
    path('uploadOrders/', views.uploadOrders, name='restaurant-uploadOrders'),
]