import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from . models import *
from django.views.decorators.csrf import csrf_exempt
# from . serializers import *
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from datetime import datetime

# Create your views here.
def home(request):

	base_url = "http://localhost:8000/maketime/"

	urls = {
		"home": base_url,
		"uploadEvents": base_url + "uploadEvents"
	}

	return JsonResponse({"urls": urls})

@csrf_exempt
def uploadEvents(request):

	log = []

	data = '[{"name":"Hello World","notes":"This is a POST request"},{"name":"Another","notes":"No ID"}]'

	file_path = 'C:\\Users\\Emily\\Documents\\01_Files\\03_Projects\\01_Python\\Python Projects\\HolidayAPI TSV\\2020.json'

	create_data = []

	with open(file_path) as json_file:
		test_data = json.load(json_file)

		for d in test_data:
			obj = {}
			obj["name"] = d["Holiday Name"]
			obj["notes"] = d["Information"]
			obj["date"] = datetime.strptime(d["Date"], '%Y%m%d').strftime('%Y-%m-%d')
			create_data.append(obj)

		# print(test_data)
		# print(create_data)

	data = json.dumps(create_data)

	if request.method != "POST":

		try:
			createdcount = 0
			updatecount = 0

			jd = json.loads(data)

			for ev in jd:
				try:
					exist = get_object_or_404(Event, name=ev["name"], date=ev["date"])

					mod, created = Event.objects.update_or_create(name=ev["name"], date=ev["date"], defaults=ev)
					updatecount += 1
				except Exception as e:
					mod, created = Event.objects.update_or_create(name=ev["name"], date=ev["date"], defaults=ev)
					createdcount += 1

			return JsonResponse({"successful": "True", "createdcount": createdcount, "updatecount": updatecount, "log": log})
		except Exception as e:
			return JsonResponse({"successful": "False", "error": str(e)})
	else:
		return JsonResponse({"successful": "False", "request": "POST"})