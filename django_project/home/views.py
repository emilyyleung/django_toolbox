from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from . import data_tools

def home(request):
	print("HOME")
	if request.method == 'GET':
		print(data_tools.data)
		data = {
			"root": [
				{
					"title": "List Compare",
					"description": "Multiline input for comparing lists",
					"logo": "fas fa-list-ol",
					"url": "http://localhost:8000/list/textarea"
				},
				{
					"title": "Kraken",
					"description": "Returns a table of files in folder",
					"logo": "far fa-folder",
					"url": "http://localhost:7000/kraken/table"
				}
			]
		}
		return render(request, "home/homepage.html", {"out": data_tools.data})
	else:
		pass
	return render(request, "home/homepage.html", {"out": "working"})