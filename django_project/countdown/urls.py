from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='countdown-home'),
    path('now', views.now, name='countdown-now'),
    url(r'^(?P<year>[\d]{4})/(?P<month>[\d]{1,2})/(?P<day>[\d]{1,2})/(?P<hour>[\d]{1,2})/$', views.count, name='countdown-count'),

    url(r'^(?P<year>[\d]{4})/$', views.count, name='countdown-count'),
    url(r'^(?P<year>[\d]{4})/(?P<month>[\d]{1,2})/$', views.count, name='countdown-count'),
    url(r'^(?P<year>[\d]{4})/(?P<month>[\d]{1,2})/(?P<day>[\d]{1,2})/$', views.count, name='countdown-count'),
    url(r'^(?P<year>[\d]{4})/(?P<month>[\d]{1,2})/(?P<day>[\d]{1,2})/(?P<hour>[\d]{1,2})/$', views.count, name='countdown-count'),
    url(r'^(?P<year>[\d]{4})/(?P<month>[\d]{1,2})/(?P<day>[\d]{1,2})/(?P<hour>[\d]{1,2})/(?P<minute>[\d]{1,2})/$', views.count, name='countdown-count'),
    url(r'^(?P<year>[\d]{4})/(?P<month>[\d]{1,2})/(?P<day>[\d]{1,2})/(?P<hour>[\d]{1,2})/(?P<minute>[\d]{1,2})/(?P<second>[\d]{1,2})/$', views.count, name='countdown-count'),

    # path('count/<year>/', views.count, name='countdown-count'),
    # path('count/<year>/<month>/', views.count, name='countdown-count'),
    # path('count/<year>/<month>/<day>/', views.count, name='countdown-count'),
    # path('count/<year>/<month>/<day>/<hour>', views.count, name='countdown-count'),
    # path('count/<year>/<month>/<day>/<hour>/<minute>', views.count, name='countdown-count'),
    # path('count/<year>/<month>/<day>/<hour>/<minute>/<second>/', views.count, name='countdown-count'),

    path('clock', views.clock, name='countdown'),

    url(r'^clock/(?P<year>[\d]{4})/$', views.clock, name='countdown-clock'),
    url(r'^clock/(?P<year>[\d]{4})/(?P<month>[\d]{1,2})/$', views.clock, name='countdown-clock'),
    url(r'^clock/(?P<year>[\d]{4})/(?P<month>[\d]{1,2})/(?P<day>[\d]{1,2})/$', views.clock, name='countdown-clock'),
    url(r'^clock/(?P<year>[\d]{4})/(?P<month>[\d]{1,2})/(?P<day>[\d]{1,2})/(?P<hour>[\d]{1,2})/$', views.clock, name='countdown-clock'),
    url(r'^clock/(?P<year>[\d]{4})/(?P<month>[\d]{1,2})/(?P<day>[\d]{1,2})/(?P<hour>[\d]{1,2})/(?P<minute>[\d]{1,2})/$', views.clock, name='countdown-clock'),
    url(r'^clock/(?P<year>[\d]{4})/(?P<month>[\d]{1,2})/(?P<day>[\d]{1,2})/(?P<hour>[\d]{1,2})/(?P<minute>[\d]{1,2})/(?P<second>[\d]{1,2})/$', views.clock, name='countdown-clock'),
]
