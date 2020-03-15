from django.contrib import admin
from . models import *

# modelAdmins

class customerAdmin(admin.ModelAdmin):
	fieldsets = [
		("Name", {"fields": ["first_name", "last_name"]}),
		("Orders", {"fields": ["orders"]})
	]
	filter_horizontal = ('orders',)

class dishAdmin(admin.ModelAdmin):
	search_fields=("name", "cost", )
	list_display = ["name", "dish_course", "cost", "vegan", "vegetarian_option", "gluten_free", "signature_dish", "spice_level", "pieces"]
	list_per_page = 10
	fieldsets = [
		("General", {"fields": ["name", "description", "dish_course", "cost"]}),
		("Properties", {"fields": ["vegan", "vegetarian_option", "gluten_free", "signature_dish", "spice_level", "pieces"]}),
	]

class courseAdmin(admin.ModelAdmin):
	list_display = ["course_name", "translation"]
	fieldsets = [
		("Name", {"fields": ["course_name", "translation"]}),
	]

class orderAdmin(admin.ModelAdmin):
	search_fields=("number",)
	list_display = ["number", "total", "date"]
	readonly_fields = ('number', 'total', 'date')
	fieldsets = [
		("Order Number", {"fields": ["number", "date"]}),
		("Order Cost", {"fields": ["total"]}),
		("Dishes", {"fields": ["dishes"]})
	]
	filter_horizontal = ('dishes',)

# Register your models here.
admin.site.register(Dish, dishAdmin)
admin.site.register(Customer, customerAdmin)
admin.site.register(Order, orderAdmin)
admin.site.register(Course, courseAdmin)