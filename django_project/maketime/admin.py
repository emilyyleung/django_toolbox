from django.contrib import admin
from . models import *

class eventAdmin(admin.ModelAdmin):
	list_display = ["id", "name", "date"]
	fieldsets = [
		("Name", {"fields": ["name", "notes"]}),
		("Date and Time", {"fields": ["date", "start_time", "end_time"]})
	]

# Register your models here.
admin.site.register(Event, eventAdmin)
admin.site.register(Calendar)