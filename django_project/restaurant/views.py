from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from . models import *
import json
from django.views.decorators.csrf import csrf_exempt
from .serializers import *
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class DishViewSet(viewsets.ModelViewSet):
	queryset = Dish.objects.all()
	serializer_class = DishSerializer
	# filter_backends = [filters.SearchFilter ,DjangoFilterBackend]
	# filterset_fields = ['project__number',]
	# search_fields = ('data_text',)

class CourseViewSet(viewsets.ModelViewSet):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer
	# filter_backends = [filters.SearchFilter ,DjangoFilterBackend]
	# filterset_fields = ['project__number',]
	# search_fields = ('data_text',)

# Create your views here.
def home(request):
	return JsonResponse({"hello": "world"})

def menu(request):
	headers_1 = ["Snacks", "Pan Fried Dumplings"]
	headers_2 = ["Rice", "Dumplings", "Soup", "Noodles"]
	headers_3 = ["Vegetables", "Mains", "Dessert"]

	all_dishes = Dish.objects.all().order_by('dish_course')

	column_1 = []
	column_2 = []
	column_3 = []

	# context = Dish.objects.all().filter(dish_course__course_name="Snacks")

	for i in headers_1:
		obj = {}
		
		course_obj = Course.objects.get(course_name=i)
		translation = course_obj.translation

		dishes = Dish.objects.all().filter(dish_course__course_name=i)
		
		obj["translation"] = translation
		obj["dishes"] = dishes

		column_1.append(obj)

	for i in headers_2:
		obj = {}
		
		course_obj = Course.objects.get(course_name=i)
		translation = course_obj.translation

		dishes = Dish.objects.all().filter(dish_course__course_name=i)
		
		obj["translation"] = translation
		obj["dishes"] = dishes

		column_2.append(obj)

	for i in headers_3:
		obj = {}
		
		course_obj = Course.objects.get(course_name=i)
		translation = course_obj.translation

		dishes = Dish.objects.all().filter(dish_course__course_name=i)
		
		obj["translation"] = translation
		obj["dishes"] = dishes

		column_3.append(obj)

	context = {"column_1": column_1, "column_2": column_2, "column_3": column_3}

	return render(request, "restaurant/menu_dishes.html", {"context": context})

def spreadsheet_example(request):
	return render(request, "restaurant/spreadsheet_4.html")

def spreadsheet(request):
	import json
	allDishes = DishSerializer(Dish.objects.all(), many=True).data
	context = {
		"data": json.dumps(allDishes)
	}
	# print(context)
	return render(request, "restaurant/spreadsheet.html", {"context": context})

@csrf_exempt
def updateDishes(request):

	log = []

	if request.method == "POST":

		# data = '[{"id":1,"name":"Blanched Edamame","description":"Light sprinkling of organic sea salt","cost":100,"vegan":true,"vegetarian_option":false,"gluten_free":false,"signature_dish":false,"spice_level":0,"pieces":0}]'

		try:
			createdcount = 0
			updatecount = 0

			data = request.POST['data']
			jd = json.loads(data)

			# print(jd)

			for d in jd:
				# print(d["dish_course"]["course_name"])
				try:
					exist = get_object_or_404(Dish, id=d["id"])

					try:
						d["dish_course"] = get_object_or_404(Course, course_name=d["dish_course"]["course_name"])
					except:
						d["dish_course"] = get_object_or_404(Course, course_name="N/A")

					mod, created = Dish.objects.update_or_create(id=d["id"], defaults=d)
					updatecount += 1
				except Exception as e:
					log.append(str(e))

					try:
						d["dish_course"] = get_object_or_404(Course, course_name=d["dish_course"]["course_name"])
					except:
						d["dish_course"] = get_object_or_404(Course, course_name="N/A")

					mod, created = Dish.objects.update_or_create(id=d["id"], defaults=d)
					createdcount += 1
			return JsonResponse({"createdcount": createdcount, "updatecount": updatecount, "log": log})
		except Exception as e:
			return JsonResponse({"unsuccessful": "True", "error": str(e), "log": log})
	return JsonResponse({"works":"GET"})

@csrf_exempt
def uploadDishes(request):

	log = []

	# data = '[{"name": "Vegetarian Spring Rolls","description": "(min. of 2 per order)","cost": "0","vegan": "False","vegetarian_option": "False","gluten_free": "False","signature_dish": "False","spice_level": "0","pieces": "1"}]'

	if request.method == "POST":
		try:
			createdcount = 0
			updatecount = 0

			data = request.POST["data"]
			# print(data)
			jd = json.loads(data)

			for d in jd:
				# print(d["dish_course"])
				try:
					exist = get_object_or_404(Dish, name=d["name"])

					try:
						d["dish_course"] = get_object_or_404(Course, course_name=d["dish_course"])
					except:
						d["dish_course"] = get_object_or_404(Course, course_name="N/A")

					mod, created = Dish.objects.update_or_create(name=d["name"], defaults=d)

					updatecount += 1
				except Exception as e:
					log.append(str(e))

					try:
						d["dish_course"] = get_object_or_404(Course, course_name=d["dish_course"])
					except:
						d["dish_course"] = get_object_or_404(Course, course_name="N/A")

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