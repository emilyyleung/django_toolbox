from django.shortcuts import render
from django.http import JsonResponse

from datetime import datetime, date

# Create your views here.
def home(request):
    return JsonResponse({"countdown":"working"})

def now(request):
	now = datetime. now()
	current_time = now. strftime("%H:%M:%S")
	return JsonResponse({"time":current_time})

def count(request, year=2019, month=1, day=1, hour=0, minute=0, second=0):
	year = int(year)
	month = int(month)
	day = int(day)
	hour = int(hour)
	minute = int(minute)
	second = int(second)

	return JsonResponse({"year": year, "month": month, "day": day, "hour": hour, "minute": minute, "seccond": second})

def clock(request, year=2020, month=2, day=1, hour=0, minute=0, second=0):

	year = int(year)
	month = int(month)
	day = int(day)
	hour = int(hour)
	minute = int(minute)
	second = int(second)

	# Dec 25, 2019 09:30:01

	# context = ",".join(variables)

	d = datetime(year, month, day, hour, minute, second).timestamp()
	# mills = time.mktime(d.timetuple())
	context = int(d) * 1000

	# context = "2020, 11, 24"

	return render(request, "countdown/countdown.html", {"dateobj": context})