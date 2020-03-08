from django.urls import path
from . import views

from django.conf.urls import url

urlpatterns = [
    path('', views.home, name='cal-home'),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    path('test/', views.test, name="test"),

	url(r'^test/(?P<year>[\d]{4})/$', views.test, name='calendar-test'),
	url(r'^test/(?P<year>[\d]{4})/(?P<month>[\d]{1,2})/$', views.test, name='calendar-test'),
	# url(r'^calendar/(?P<year>[\d]{4})/(?P<month>[\d]{1,2})/(?P<day>[\d]{1,2})/$', views.test, name='calendar-test'),

	path('year/', views.year, name="year"),
	url(r'^year/(?P<year>[\d]{4})/$', views.year, name='calendar-year'),
]
