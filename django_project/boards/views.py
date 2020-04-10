from django.shortcuts import render
from django.http import JsonResponse

import requests
import urllib
import json

# Functions

import numpy as np
# import Image

def palette(img):
	"""
	Return palette in descending order of frequency
	"""
	arr = np.asarray(img)
	palette, index = np.unique(asvoid(arr).ravel(), return_inverse=True)
	palette = palette.view(arr.dtype).reshape(-1, arr.shape[-1])
	count = np.bincount(index)
	order = np.argsort(count)
	return palette[order[::-1]]

def asvoid(arr):
	"""View the array as dtype np.void (bytes)
	This collapses ND-arrays to 1D-arrays, so you can perform 1D operations on them.
	http://stackoverflow.com/a/16216866/190597 (Jaime)
	http://stackoverflow.com/a/16840350/190597 (Jaime)
	Warning:
	>>> asvoid([-0.]) == asvoid([0.])
	array([False], dtype=bool)
	"""
	arr = np.ascontiguousarray(arr)
	return arr.view(np.dtype((np.void, arr.dtype.itemsize * arr.shape[-1])))


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
		obj = {}
		obj["photo"] = img["urls"]["regular"]
		# unsplash_photos.append(img)
		response = requests.get(img["urls"]["thumb"])
		img = Image.open(BytesIO(response.content))
		# Extract 6 colors from an image.
		colours = colorgram.extract(img, 6)
		out_colours = []
		for colour in colours:
			rgb_col = colour.rgb
			rgb_col = '#%02x%02x%02x' % rgb_col
			out_colours.append(rgb_col)
		obj["colours"] = out_colours
		print(out_colours)
		unsplash_photos.append(obj)

	# unsplash_photos = [
	# 	{
	# 		"photo": "https://images.unsplash.com/reserve/bOvf94dPRxWu0u3QsPjF_tree.jpg?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=400&fit=max&ixid=eyJhcHBfaWQiOjEyNTA0MH0",
	# 		"colours": ["#c5cec8", "#7da235", "#5a7b25", "#9ebcb4", "#98b662", "#4d673d"]
	# 	}
	# ]

	# return JsonResponse({"unsplash_data": unsplash_photos})
	return render(request, url, {"unsplash_data": unsplash_photos})

def colour_palette(request, version, query="", howMany=10):

	from colorthief import ColorThief
	
	from PIL import Image
	import requests
	# from io import BytesIO

	import io

	from urllib.request import urlopen

	url = "boards/grid/example_" + version + ".html"

	context = {}

	if query:
		unsplash_query = query
	else:
		unsplash_query = "random"
		
	unsplash_url = "https://api.unsplash.com/search/photos?page=1&per_page=" + str(howMany) + "&query=" + unsplash_query + "&client_id=" + CLIENT_ID

	r = requests.get(unsplash_url)
	job = r.json()

	unsplash_photos = []

	for img in job["results"]:
		obj = {}
		obj["photo"] = img["urls"]["regular"]
		# unsplash_photos.append(img)
		# response = requests.get(img["urls"]["small"])
		# img = Image.open(BytesIO(response.content))
		

		fd = urlopen(img["urls"]["thumb"])
		f = io.BytesIO(fd.read())
		color_thief = ColorThief(f)
		# get the dominant color
		dominant_color = color_thief.get_color(quality=1)
		# build a color palette
		palette = color_thief.get_palette(color_count=6)
		obj["colours"] = []
		for col in palette:
			rgb = '#%02x%02x%02x' % col
			obj["colours"].append(rgb)
		print(dominant_color)
		print(palette)
		unsplash_photos.append(obj)


		
	return render(request, url, {"unsplash_data": unsplash_photos})

	# return JsonResponse({"out": job, "unsplash_data": unsplash_photos})

def colourThief(request):
	return render(request, "boards/colourThief/base.html")

def test(request, version, query="", howMany=10):

	url = "boards/colourThief/CT_" + version + ".html"

	# context = {}

	# if query:
	# 	unsplash_query = query
	# else:
	# 	unsplash_query = "random"
		
	# unsplash_url = "https://api.unsplash.com/search/photos?page=1&per_page=" + str(howMany) + "&query=" + unsplash_query + "&client_id=" + CLIENT_ID

	# print(unsplash_query)

	# r = requests.get(unsplash_url)
	# job = r.json()

	unsplash_photos = []

	# for img in job["results"]:
	# 	unsplash_photos.append(img)

	# return JsonResponse({"unsplash_data": unsplash_photos})
	return render(request, url, {"unsplash_data": unsplash_photos})