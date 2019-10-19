from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from . import data_tools

def home(request):
	print("HOME")
	if request.method == 'GET':
		# print(data_tools.data)
		return render(request, "home/homepage.html", {"out": data_tools.data})
	else:
		pass
	return render(request, "home/homepage.html", {"out": "working"})