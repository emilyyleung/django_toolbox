from django.urls import path
from . import views

app_name = 'jsonmaker'

urlpatterns = [
    path('home/', views.jsonhome, name='json-home'),
    path('bulkrename/', views.bulkrename, name='json-setup'),
    path('build/', views.jsonmake, name='json-maker'),
    path('convert/', views.convert, name='json-convert'),
]