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
	fieldsets = [
		("General", {"fields": ["name", "description", "cost"]}),
		("Properties", {"fields": ["vegan", "vegetarian_option", "gluten_free", "signature_dish", "spice_level", "pieces"]}),
	]

class orderAdmin(admin.ModelAdmin):
	readonly_fields = ('number', 'total')
	fieldsets = [
		("Order Number", {"fields": ["number"]}),
		("Order Cost", {"fields": ["total"]}),
		("Dishes", {"fields": ["dishes"]})
	]
	filter_horizontal = ('dishes',)

# Register your models here.
admin.site.register(Dish, dishAdmin)
admin.site.register(Customer, customerAdmin	)
admin.site.register(Order, orderAdmin)