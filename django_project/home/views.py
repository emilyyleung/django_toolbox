from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from . import data_tools, data_emojis

def home(request):
	print("HOME")
	if request.method == 'GET':
		# print(data_tools.data)
		return render(request, "home/homepage_emoji.html", {"out": data_emojis.data})
	else:
		pass
	return render(request, "home/homepage.html", {"out": "working"})