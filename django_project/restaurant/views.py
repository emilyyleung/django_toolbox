from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from . models import *
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
	return JsonResponse({"hello": "world"})

def menu(request):
	context = Dish.objects.all()
	return render(request, "restaurant/menu_base.html", {"context": context})

@csrf_exempt
def uploadDishes(request):

	log = []

	# data = '[{"name": "Vegetarian Spring Rolls","description": "(min. of 2 per order)","cost": "0","vegan": "False","vegetarian_option": "False","gluten_free": "False","signature_dish": "False","spice_level": "0","pieces": "1"}]'

	if request.method == "POST":
		try:
			createdcount = 0
			updatecount = 0

			data = request.POST["data"]
			jd = json.loads(data)

			for d in jd:
				try:
					exist = get_object_or_404(Dish, name=d["name"])

					mod, created = Dish.objects.update_or_create(name=d["name"], defaults=d)

					updatecount += 1
				except Exception as e:
					log.append(str(e))

					mod, created = Dish.objects.update_or_create(name=d["name"], defaults=d)

					createdcount += 1
			return JsonResponse({"createdcount": createdcount, "updatecount": updatecount, "log": log})
		except Exception as e:
			return JsonResponse({"unsuccessful": "True", "error": str(e)})

	else:
		return JsonResponse({"upload dishes": "unsuccessful"})

@csrf_exempt
def uploadCustomers(request):

	log = []

	# data = '[{"first_name": "Leanne", "last_name": "Graham"}, {"first_name": "Ervin", "last_name": "Howell"}]'

	if request.method == "POST":
		try:
			createdcount = 0
			updatecount = 0

			data = request.POST["data"]
			jd = json.loads(data)

			for d in jd:
				try:
					exist = get_object_or_404(Customer, first_name=d["first_name"], last_name=d["last_name"])

					mod, created = Customer.objects.update_or_create(first_name=d["first_name"], last_name=d["last_name"], defaults=d)

					updatecount += 1
				except Exception as e:
					log.append(str(e))

					mod, created = Customer.objects.update_or_create(first_name=d["first_name"], last_name=d["last_name"], defaults=d)

					createdcount += 1
			return JsonResponse({"createdcount": createdcount, "updatecount": updatecount, "log": log})
		except Exception as e:
			return JsonResponse({"unsuccessful": "True", "error": str(e)})

	else:
		return JsonResponse({"upload customers": "unsuccessful"})

@csrf_exempt
def uploadOrders(request):

	log = []

	data = '[{"id": 15, "dishes": ["Mango Pudding"]}, {"id": 16, "dishes": ["Steamed Barramundi"]}]'

	if request.method != "POST":
		try:
			createdcount = 0
			updatecount = 0

			# data = request.POST["data"]
			jd = json.loads(data)

			for d in jd:
				try:
					exist = get_object_or_404(Order, number=d["id"])

					# mod, created = Order.objects.update_or_create(number=d["id"] ,defaults=d)

					updatecount += 1

					try:
						exist.dishes.clear()
						
						for i in d["dishes"]:
							dish = Dish.objects.get(name=i)
							exist.dishes.add(dish)

					except Exception as e:
						log.append(str(e))

				except Exception as e:
					log.append(str(e))

					mod, created = Order.objects.update_or_create(id=d["id"], defaults=d)

					createdcount += 1

					try:
						exist.dishes.clear()

						for i in d["dishes"]:
							dish = Dish.objects.get(name=i)

							exist.dishes.add(dish)

					except Exception as e:
						log.append(str(e))
			return JsonResponse({"createdcount": createdcount, "updatecount": updatecount, "log": log})
		except Exception as e:
			return JsonResponse({"unsuccessful": "True", "error": str(e), "log": log})

	else:
		return JsonResponse({"upload customers": "unsuccessful"})