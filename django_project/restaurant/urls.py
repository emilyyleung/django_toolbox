from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path
from . import views

router = routers.DefaultRouter()
router.register(r'dishes', views.DishViewSet)

app_name = 'restaurant'

urlpatterns = [
	path('', views.home, name='restaurant-home'),
	path('menu/', views.menu, name='restaurant-menu'),

	path('uploadDishes/', views.uploadDishes, name='restaurant-uploadDishes'),
	path('uploadCustomers/', views.uploadCustomers, name='restaurant-uploadCustomers'),
	path('uploadOrders/', views.uploadOrders, name='restaurant-uploadOrders'),
	path('updateDishes/', views.updateDishes, name='restaurant-updateDishes'),

	path('spreadsheet_example/', views.spreadsheet_example, name='restaurant-spreadsheet_example'),
	path('spreadsheet/', views.spreadsheet, name='restaurant-spreadsheet'),

	url(r'^', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls')),
]