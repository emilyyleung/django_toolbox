from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Event(models.Model):
	name = models.CharField(max_length=200, default="test")
	date = models.DateField(default=timezone.now())
	start_time = models.TimeField(default=datetime.time(0))
	end_time = models.TimeField(default=datetime.time(23,59,59))
	description = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.name