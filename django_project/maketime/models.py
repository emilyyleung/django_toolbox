import django
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from multiselectfield import MultiSelectField
from django.core.validators import int_list_validator, RegexValidator
from django.core.validators import validate_comma_separated_integer_list

import datetime
from dateutil.tz import *
import pytz
from . utils import allTimeZones
from dateutil.rrule import *

class CalEvent(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	
	def __str__(self):
		return self.title


class Event(models.Model):
	name = models.CharField(max_length=200, default="test")
	notes = models.TextField(blank=True, null=True)
	start_time = models.DateTimeField(default=django.utils.timezone.now)
	end_time = models.DateTimeField(default=django.utils.timezone.now)

	def __str__(self):
		return self.name

frequency_choices = (
	('YEARLY','Yearly'),
	('MONTHLY','Monthly'),
	('WEEKLY','Weekly'),
	('DAILY','Daily'),
)

frequency_lut = {
	'YEARLY':YEARLY,
	'MONTHLY':MONTHLY,
	'WEEKLY':WEEKLY,
	'DAILY':DAILY,
}

day_choices = (
	('RRule.MO','Monday'),
	('RRule.TU','Tuesday'),
	('RRule.WE','Wednesday'),
	('RRule.TH','Thursday'),
	('RRule.FR','Friday'),
	('RRule.SA','Saturday'),
	('RRule.SU','Sunday'),
)

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

bymonth_choices = (
	('Jan','January'),
	('Feb','February'),
	('Mar','March'),
	('Apr','April'),
	('May','May'),
	('Jun','June'),
	('Jul','July'),
	('Aug','August'),
	('Sep','September'),
	('Oct','October'),
	('Nov','November'),
	('Dec','December'),
)

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

timezone_choices = allTimeZones()

end_of_year = datetime.datetime.now().replace(month=12,day=31,hour=23,minute=59,second=59)

# Create your models here.
class Calendar(models.Model):
	name = models.CharField(max_length=100)
	priority = models.IntegerField(
		default=0,
		validators=[
			MaxValueValidator(100),
			MinValueValidator(0)
		]
	)

	def __str__(self):
		return self.name

class Recurrence(models.Model):
	frequency = models.CharField(max_length=200, choices=frequency_choices)
	dtstart = models.DateTimeField(default=django.utils.timezone.now)
	tzid = models.CharField(max_length=200, choices=timezone_choices)
	until = models.DateTimeField(default=end_of_year)
	count = models.IntegerField(default=0, validators=[MinValueValidator(0)])
	interval = models.IntegerField(default=1, validators=[MinValueValidator(1)])
	wkst = models.CharField(max_length=200, choices=day_choices, default="RRule.MO")

	byweekday = MultiSelectField(choices=day_choices, blank=True, null=True)
	bymonth = MultiSelectField(choices=bymonth_choices, blank=True, null=True)
	bysetpos = models.CharField(validators=[RegexValidator(regex='^-?[-?\d,]+$')], max_length=100, blank=True, null=True)
	bymonthday = models.CharField(validators=[RegexValidator(regex='^-?[-?\d,]+$')], max_length=100, blank=True, null=True)
	byyearday = models.CharField(validators=[RegexValidator(regex='^-?[-?\d,]+$')], max_length=100, blank=True, null=True)
	byweekno = models.CharField(validators=[RegexValidator(regex='^-?[-?\d,]+$')], max_length=100, blank=True, null=True)

	def r_frequency(self):
		return frequency_lut[str(self.frequency)]

	def r_wkst(self):
		return day_lut[self.wkst]

	def r_count(self):
		if self.count == 0:
			r_count = None
		else:
			r_count = self.count
		return r_count

	def r_byweekday(self):
		try:
			multibyweekday = str(self.byweekday).split(', ')
		except Exception as e:
			multibyweekday = str(self.byweekday)

		if len(multibyweekday) > 0 and multibyweekday[0] != "None" and multibyweekday[0] != "":
			r_byweekday = []
			for day in multibyweekday:
				day_num = weekday_lut[day]
				r_byweekday.append(day_num)
		else:
			r_byweekday = None

		return r_byweekday

	def r_bymonth(self):
		try:
			multibymonth = str(self.bymonth).split(', ')
		except Exception as e:
			multibymonth = str(self.bymonth)

		if len(multibymonth) > 0 and multibymonth[0] != "None" and multibymonth[0] != "":
			r_bymonth = []
			for month in multibymonth:
				month_num = month_lut[month]
				r_bymonth.append(month_num)
		else:
			r_bymonth = None

		return r_bymonth

	def r_bysetpos(self):
		try:
			multibysetpos = self.bysetpos.split(',')
			r_bysetpos = [int(x) for x in multibysetpos]
		except:
			multibysetpos = self.bysetpos
			print(multibysetpos)
			if multibysetpos == None:
				r_bysetpos = None
			else:
				r_bysetpos = [int(x) for x in multibysetpos]

		return r_bysetpos

	def r_bymonthday(self):
		try:
			multibymonthday = self.bymonthday.split(',')
			r_bymonthday = [int(x) for x in multibymonthday]
		except:
			multibymonthday = self.bymonthday
			if multibymonthday == None:
				r_bymonthday = None
			else:
				r_bymonthday = [int(x) for x in multibymonthday]

		return r_bymonthday

	def r_byyearday(self):
		try:
			multibyyearday = self.byyearday.split(',')
			r_byyearday = [int(x) for x in multibyyearday]
		except:
			multibyyearday = self.byyearday
			if multibyyearday == None:
				r_byyearday = None
			else:
				r_byyearday = [int(x) for x in multibyyearday]

		return r_byyearday

	def r_byweekno(self):
		try:
			multibyweekno = self.byweekno.split(',')
			r_byweekno = [int(x) for x in multibyweekno]
		except:
			multibyweekno = self.byweekno
			if multibyweekno == None:
				r_byweekno = None
			else:
				r_byweekno = [int(x) for x in multibyweekno]

		return r_byweekno

	def r_ruleset(self):
		print("hello1")
		out = []

		try:
			ruleset = list(rrule(
				freq=self.r_frequency(),
				dtstart=self.dtstart,
				until=self.until,
				count=self.r_count(),
				interval=self.interval,
				wkst=self.r_wkst(),
				byweekday=self.r_byweekday(),
				bymonth=self.r_bymonth(),
				bysetpos=self.r_bysetpos(),
				bymonthday=self.r_bymonthday(),
				byyearday=self.r_byyearday(),
				byweekno=self.r_byweekno(),
			))

			print("ruleset")
			print(ruleset)

			for dt in ruleset:
				print(dt)
				out.append(dt)

		except Exception as e:
			print("hello2")
			print(e)

		# print(out)
		print(out)

		return out