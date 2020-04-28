from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def home(request):

	base_url = "http://localhost:8000/maketime/"

	urls = {
		"home": base_url
	}

	return JsonResponse({"urls": urls})