from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='list-home'),
    path('comma/', views.sepComma, name='list-comma'),
    path('multiline/', views.sepMulti, name='list-multiline'),
    path('textarea/', views.sepTextarea, name='list-textarea')
]