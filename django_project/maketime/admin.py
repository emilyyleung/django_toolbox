from django.contrib import admin
from . models import *

class eventAdmin(admin.ModelAdmin):
	list_display = ["id", "name"]
	fieldsets = [
		("Name", {"fields": ["name", "notes"]}),
	]

class recurrenceAdmin(admin.ModelAdmin):
	readonly_fields = ("r_frequency","r_wkst","r_count","r_byweekday","r_bymonth","r_bysetpos","r_bymonthday","r_byyearday","r_byweekno","r_ruleset",)
	list_display = ["id", "frequency", "dtstart", "until", "count"]
	fieldsets = [
		("Required", {"fields": ["frequency","dtstart","tzid","until","count","interval","wkst",]}),
		("Functions", {"fields": ["r_frequency","r_wkst","r_count","r_byweekday","r_bymonth","r_bysetpos","r_bymonthday","r_byyearday","r_byweekno","r_ruleset",]}),
		("Optional", {"fields": ["byweekday","bymonth","bysetpos","bymonthday","byyearday","byweekno",]}),
	]


# Register your models here.
admin.site.register(Event, eventAdmin)
admin.site.register(Calendar)
admin.site.register(CalEvent)
admin.site.register(Recurrence, recurrenceAdmin)
