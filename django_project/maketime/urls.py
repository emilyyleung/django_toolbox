from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'maketime'

urlpatterns = [
	path('', views.home, name='maketime-home'),
	path('uploadEvents/', views.uploadEvents, name='maketime-uploadEvents'),
]