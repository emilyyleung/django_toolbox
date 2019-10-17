from django.urls import path
from . import views

from django.conf.urls import url

urlpatterns = [
    path('', views.home, name='cal-home'),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
]
