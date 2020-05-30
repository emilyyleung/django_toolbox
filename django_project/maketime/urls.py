from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'maketime'

urlpatterns = [
	path('', views.home, name='maketime-home'),
	path('uploadEvents/', views.uploadEvents, name='maketime-uploadEvents'),
	path('recurringEvents/', views.recurringEvents, name='maketime-recurringEvents'),
	path('testEvents/', views.testEvents, name='maketime-testEvents'),
	# path('calendarView/', views.calendarView, name='maketime-calendarView'),
	path('calendarView/<str:year>/<str:month>/', views.calendarView, name='maketime-calendarView'),
]