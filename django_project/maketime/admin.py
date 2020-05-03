from django.contrib import admin
from . models import *

class eventAdmin(admin.ModelAdmin):
	list_display = ["id", "name"]
	fieldsets = [
		("Name", {"fields": ["name", "notes"]}),
	]

class recurrenceAdmin(admin.ModelAdmin):
	list_display = ["id", "frequency", "dtstart", "until", "count"]
	fieldsets = [
		("Required", {"fields": ["frequency","dtstart","tzid","until","count","interval","wkst",]}),
		("Optional", {"fields": ["byweekday","bymonth","bysetpos","testbysetpos","bymonthday","byyearday","byweekno",]})
	]


# Register your models here.
admin.site.register(Event, eventAdmin)
admin.site.register(Calendar)
admin.site.register(Recurrence, recurrenceAdmin)
