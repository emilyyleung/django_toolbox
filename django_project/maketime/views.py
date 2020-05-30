import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from . models import *
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from datetime import datetime

from dateutil.rrule import *
import pytz
import dateutil.parser

import calendar
from django.utils.safestring import mark_safe
from . utils import Calendar, CustomHTMLCalendar
from django.views import generic

# Create your views here.
def home(request):

	base_url = "http://localhost:8000/maketime/"

	urls = {
		"home": base_url,
		"uploadEvents": base_url + "uploadEvents",
		"recurringEvents": base_url + "recurringEvents",
		"testEvents": base_url + "testEvents",
		"calendarView": base_url + "calendarView",
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

def convert_datetime_timezone(dt, tz1, tz2):
	tz1 = pytz.timezone(tz1)
	tz2 = pytz.timezone(tz2)

	dt = datetime.strptime(dt,"%Y-%m-%d %H:%M:%S")
	dt = tz1.localize(dt)
	dt = dt.astimezone(tz2)
	dt = dt.strftime("%Y-%m-%d %H:%M:%S")

	return dt

def recurringEvents(request):

	frequency_lut = {
		'YEARLY':YEARLY,
		'MONTHLY':MONTHLY,
		'WEEKLY':WEEKLY,
		'DAILY':DAILY,
	}

	day_lut = {
		'RRule.MO': MO,
		'RRule.TU': TU,
		'RRule.WE': WE,
		'RRule.TH': TH,
		'RRule.FR': FR,
		'RRule.SA': SA,
		'RRule.SU': SU,
	}

	weekday_lut = {
		'Monday': MO,
		'Tuesday': TU,
		'Wednesday': WE,
		'Thursday': TH,
		'Friday': FR,
		'Saturday': SA,
		'Sunday': SU,
	}

	month_lut = {
		'January': 1,
		'February': 2,
		'March': 3,
		'April': 4,
		'May': 5,
		'June': 6,
		'July': 7,
		'August': 8,
		'September': 9,
		'October': 10,
		'November': 11,
		'December': 12,
	}

	out = []

	rules = Recurrence.objects.all()
	tz = pytz.timezone("Australia/Sydney")

	start_date = datetime(2020, 1, 1, 0, 0, 0)
	end_date = datetime(2020, 12, 8, 0, 0, 0)

	for rule in rules:

		obj = []

		# r_frequency = frequency_lut[str(rule.frequency)]
		r_frequency = rule.r_frequency()
		print("r_frequency")
		print(r_frequency)

		r_dtstart = rule.dtstart
		print(r_dtstart)
		con_r_dtstart = convert_datetime_timezone(str(r_dtstart), "UTC", rule.tzid)
		datetime_dtstart = datetime.strptime(con_r_dtstart, '%Y-%m-%d %H:%M:%S')
		print(datetime_dtstart)

		r_until = rule.until
		# print(r_until)
		con_r_until = convert_datetime_timezone(str(r_until), "UTC", rule.tzid)
		datetime_until = datetime.strptime(con_r_until, '%Y-%m-%d %H:%M:%S')
		# print(datetime_until)

		r_wkst = day_lut[rule.wkst]

		if rule.count == 0:
			r_count = None
		else:
			r_count = rule.count

		try:
			multibyweekday = str(rule.byweekday).split(', ')
		except Exception as e:
			multibyweekday = str(rule.byweekday)

		print(multibyweekday)

		if len(multibyweekday) > 0 and multibyweekday[0] != "None" and multibyweekday[0] != "":
			r_byweekday = []
			for day in multibyweekday:
				day_num = weekday_lut[day]
				r_byweekday.append(day_num)
		else:
			r_byweekday = None

		try:
			multibymonth = str(rule.bymonth).split(', ')
		except Exception as e:
			multibymonth = str(rule.bymonth)

		if len(multibymonth) > 0 and multibymonth[0] != "None" and multibymonth[0] != "":
			r_bymonth = []
			for month in multibymonth:
				month_num = month_lut[month]
				r_bymonth.append(month_num)
		else:
			r_bymonth = None

		r_interval = rule.interval

		# r_bysetpos = rule.bysetpos
		try:
			multibysetpos = rule.bysetpos.split(',')
			r_bysetpos = [int(x) for x in multibysetpos]
		except:
			multibysetpos = rule.bysetpos
			print(multibysetpos)
			if multibysetpos == None:
				r_bysetpos = None
			else:
				r_bysetpos = [int(x) for x in multibysetpos]

		print(r_bysetpos)

		try:
			multibymonthday = rule.bymonthday.split(',')
			r_bymonthday = [int(x) for x in multibymonthday]
		except:
			multibymonthday = rule.bymonthday
			if multibymonthday == None:
				r_bymonthday = None
			else:
				r_bymonthday = [int(x) for x in multibymonthday]

		try:
			multibyyearday = rule.byyearday.split(',')
			r_byyearday = [int(x) for x in multibyyearday]
		except:
			multibyyearday = rule.byyearday
			if multibyyearday == None:
				r_byyearday = None
			else:
				r_byyearday = [int(x) for x in multibyyearday]

		try:
			multibyweekno = rule.byweekno.split(',')
			r_byweekno = [int(x) for x in multibyweekno]
		except:
			multibyweekno = rule.byweekno
			if multibyweekno == None:
				r_byweekno = None
			else:
				r_byweekno = [int(x) for x in multibyweekno]

		ruleset = list(rrule(
			freq=r_frequency,
			# dtstart=datetime_dtstart,
			# until=datetime_until,
			dtstart=r_dtstart,
			until=r_until,
			count=r_count,
			interval=r_interval,
			wkst=r_wkst,
			byweekday=r_byweekday,
			bymonth=r_bymonth,
			bysetpos=r_bysetpos,
			bymonthday=r_bymonthday,
			byyearday=r_byyearday,
			byweekno=r_byweekno,
		))

		# print(r_frequency, r_dtstart.astimezone(tz), r_until.astimezone(tz), r_count, r_interval, r_wkst, r_byweekday, r_bymonth)

		for dt in ruleset:
			# print(dt)
			obj.append(dt)
		out.append(obj)

	#######################################################

	bday = datetime(1996,12,8, 0, 0, 0)
	print(WEEKLY, start_date, end_date, None, 1, MO, None, 4)

	test_ruleset = list(rrule(
		freq=WEEKLY,
		dtstart=start_date,
		until=end_date,
		count=None,
		interval=1,
		wkst=MO,
		byweekday=None,
		bymonth=4
	))


	print("----------------------------------------")
	print(WEEKLY)
	print("----------------------------------------")

	for dt in test_ruleset:
		# print(dt)
		# obj.append(dt)
		print(dt.astimezone(tz))
		# obj.append(dt.astimezone(tz))

	return JsonResponse({"out": out})

def testEvents(request):

	out = []

	recurrences = Recurrence.objects.all()

	for recurrence in recurrences:
		arr = []
		try:
			ruleset = list(rrule(
				freq=recurrence.r_frequency(),
				dtstart=recurrence.dtstart,
				until=recurrence.until,
				count=recurrence.r_count(),
				interval=recurrence.interval,
				wkst=recurrence.r_wkst(),
				byweekday=recurrence.r_byweekday(),
				bymonth=recurrence.r_bymonth(),
				bysetpos=recurrence.r_bysetpos(),
				bymonthday=recurrence.r_bymonthday(),
				byyearday=recurrence.r_byyearday(),
				byweekno=recurrence.r_byweekno(),
			))

			for dt in ruleset:
				print(dt)
				arr.append(dt)

			out.append(arr)

		except Exception as e:
			print("hello2")
			print(e)

	return JsonResponse({"out": out})

def calendarView(request, year=2020, month=5):

	# c = calendar.HTMLCalendar(calendar.SUNDAY)
	# html_cal = c.formatmonth(2020,1)
	# context = {"calendar": html_cal}

	# print(calendar.monthcalendar(1983, 11))

	month_lut = {
		1: "JANUARY",
		2: "FEBRUARY",
		3: "MARCH",
		4: "APRIL",
		5: "MAY",
		6: "JUNE",
		7: "JULY",
		8: "AUGUST",
		9: "SEPTEMBER",
		10: "OCTOBER",
		11: "NOVEMBER",
		12: "DECEMBER",
	}
	
	events_obj = {
		1: ["hello world", "hey there", "Dinner Party", "Wedding!"],
		10: ["bye world"],
		18: ["Dinner Party", "Wedding!", "Bowling", "Basketball Game", "Surfing"],
		24: ["Happy birthday!"]
	}
	
	cal_data = calendar.monthcalendar(int(year), int(month))
	month_arr = []
	for week in cal_data:
		week_arr = []
		for day in week:
			obj = {"Day": day}
			if day in events_obj.keys():
				obj["Events"] = events_obj[day]
			week_arr.append(obj)
		month_arr.append(week_arr)

	print(month_arr)



	out = calendar.monthcalendar(2020, 5)
	context = {"calendar": out}

	context["event_calendar"] = month_arr
	context["month"] = month_lut[int(month)] + " " + str(year)

	return render(request, "maketime/full_calendar.html", context)