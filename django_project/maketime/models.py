import django
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from multiselectfield import MultiSelectField
from django.core.validators import int_list_validator
from django.core.validators import validate_comma_separated_integer_list

import datetime
from dateutil.tz import *
import pytz
from . utils import allTimeZones

frequency_choices = (
	('YEARLY','Yearly'),
	('MONTHLY','Monthly'),
	('WEEKLY','Weekly'),
	('DAILY','Daily'),
)

day_choices = (
	('RRule.MO','Monday'),
	('RRule.TU','Tuesday'),
	('RRule.WE','Wednesday'),
	('RRule.TH','Thursday'),
	('RRule.FR','Friday'),
	('RRule.SA','Saturday'),
	('RRule.SU','Sunday'),
)

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
	# byweekday = models.CharField(max_length=200, choices=day_choices, blank=True, null=True)
	# bymonth = models.CharField(max_length=200, choices=bymonth_choices, blank=True, null=True)
	bymonth = MultiSelectField(choices=bymonth_choices, blank=True, null=True)
	bysetpos = models.CharField(max_length=200, blank=True, null=True)
	bymonthday = models.CharField(max_length=200, blank=True, null=True)
	byyearday = models.CharField(max_length=200, blank=True, null=True)
	byweekno = models.CharField(max_length=200, blank=True, null=True)

	bysetpos = models.CharField(validators=[int_list_validator()], max_length=100, blank=True, null=True)
	testbysetpos = models.CharField(validators=[validate_comma_separated_integer_list], max_length=100, blank=True, null=True)

class Event(models.Model):
	name = models.CharField(max_length=200, default="test")
	notes = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.name