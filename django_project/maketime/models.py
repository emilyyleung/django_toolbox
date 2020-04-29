from django.db import models
from django.utils import timezone
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Event(models.Model):
	name = models.CharField(max_length=200, default="test")
	date = models.DateField(default=timezone.now())
	start_time = models.TimeField(default=datetime.time(0))
	end_time = models.TimeField(default=datetime.time(23,59,59))
	notes = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.name

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