from django.shortcuts import render
from django.http import JsonResponse

import requests
import urllib
import json

# Create your views here.
def home(request):
	return JsonResponse({"Hello": "world"})

CLIENT_ID = "BKz4sZ9bEWqEPHvdaJFfcmo5e0eXV06t3_0Xi06GQt4"

def muuri_example(request, version, query="", howMany=10):
	url = "boards/muuri_example/example_" + version + ".html"

	context = {}

	if query:
		unsplash_query = query
	else:
		unsplash_query = "random"
		
	unsplash_url = "https://api.unsplash.com/search/photos?page=1&per_page=" + str(howMany) + "&query=" + unsplash_query + "&client_id=" + CLIENT_ID

	print(unsplash_query)

	r = requests.get(unsplash_url)
	job = r.json()

	unsplash_photos = []

	for img in job["results"]:
		unsplash_photos.append(img)

	# return JsonResponse({"response": job, "unsplash_data": unsplash_photos})
	return render(request, url, {"unsplash_data": unsplash_photos})

def grid_of_squares(request, version, query="", howMany=10):

	import colorgram
	
	from PIL import Image
	import requests
	from io import BytesIO

	url = "boards/grid/example_" + version + ".html"

	context = {}

	if query:
		unsplash_query = query
	else:
		unsplash_query = "random"
		
	unsplash_url = "https://api.unsplash.com/search/photos?page=1&per_page=" + str(howMany) + "&query=" + unsplash_query + "&client_id=" + CLIENT_ID

	print(unsplash_query)

	r = requests.get(unsplash_url)
	job = r.json()

	unsplash_photos = []

	for img in job["results"]:
		unsplash_photos.append(img)
		response = requests.get(img["urls"]["small"])
		img = Image.open(BytesIO(response.content))
		# Extract 6 colors from an image.
		colours = colorgram.extract(img, 6)
		out_colours = []
		for colour in colours:
			rgb_col = colour.rgb
			rgb_col = '#%02x%02x%02x' % rgb_col
			out_colours.append(rgb_col)
		print(out_colours)
		unsplash_photos.append(out_colours)
	
	# colour_palettes = []

	# for photo in unsplash_photos:
	# 	response = requests.get(photo["urls"]["small"])
	# 	img = Image.open(BytesIO(response.content))
	# 	# Extract 6 colors from an image.
	# 	colours = colorgram.extract(img, 6)
	# 	out_colours = []
	# 	for colour in colours:
	# 		rgb_col = colour.rgb
	# 		rgb_col = '#%02x%02x%02x' % rgb_col
	# 		out_colours.append(rgb_col)
	# 	colour_palettes.append(out_colours)

	# 	print(out_colours)


	return JsonResponse({"response": job, "unsplash_data": unsplash_photos})
	# return render(request, url, {"unsplash_data": unsplash_photos})