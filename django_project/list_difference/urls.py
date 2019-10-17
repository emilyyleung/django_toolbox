from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='list-home'),
    path('app/', views.form, name='list-form')
]