from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from datetime import datetime
from django.views import generic
from django.utils.safestring import mark_safe

from . models import *
from . utils import Calendar

import calendar

def home(request):
    return JsonResponse({"hello": "world"})

class CalendarView(generic.ListView):
    model = Event
    template_name = 'cal/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

####################################################################

def test(request, year=2020, month=1):

    # hc = calendar.HTMLCalendar(calendar.THURSDAY)
    # hc = calendar.HTMLCalendar(firstweekday = 0)
    hc = calendar.HTMLCalendar(calendar.SUNDAY)

    cal_str = hc.formatmonth(int(year), int(month))

    return HttpResponse(cal_str)

def year(request, year=2020):
    text_cal = calendar.HTMLCalendar(firstweekday = 0) 
    cal_str = text_cal.formatyearpage(int(year), width=1)

    return HttpResponse(cal_str)