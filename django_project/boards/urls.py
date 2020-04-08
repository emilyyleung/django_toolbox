from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	path('', views.home, name='boards-home'),
	path('muuri_example/<str:version>/', views.muuri_example, name='boards-muuri_example'),
	path('muuri_example/<str:version>/<str:query>/', views.muuri_example, name='boards-muuri_example'),
	path('muuri_example/<str:version>/<str:query>/<str:howMany>/', views.muuri_example, name='boards-muuri_example'),

	# path('grid/', views.grid_of_squares, name='boards-grid_of_squares'),
	path('grid/<str:version>/', views.grid_of_squares, name='boards-grid_of_squares'),
	path('grid/<str:version>/<str:query>/', views.grid_of_squares, name='boards-grid_of_squares'),
	path('grid/<str:version>/<str:query>/<str:howMany>/', views.grid_of_squares, name='boards-grid_of_squares'),

	path('polaroid/<str:version>/', views.colour_palette, name='boards-colour_palette'),
	path('polaroid/<str:version>/<str:query>/', views.colour_palette, name='boards-colour_palette'),
	path('polaroid/<str:version>/<str:query>/<str:howMany>/', views.colour_palette, name='boards-colour_palette'),

	path('colourThief/', views.colourThief, name='boards-colourThief'),
]