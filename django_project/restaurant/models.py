from django.db import models
from . ultils import get_default_course

class Course(models.Model):
	course_name = models.CharField(max_length=200)
	translation = models.CharField(max_length=5)

	def __str__(self):
		return self.course_name

# Create your models here.
class Dish(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(default="")

	dish_course = models.ForeignKey(Course, default=get_default_course(Course), on_delete=models.SET_DEFAULT)

	cost = models.DecimalField(max_digits=99999, decimal_places=2)

	vegan = models.BooleanField(default=False)
	vegetarian_option = models.BooleanField(default=False)
	gluten_free = models.BooleanField(default=False)
	signature_dish = models.BooleanField(default=False)
	spice_level = models.IntegerField(default=0)
	pieces = models.IntegerField(default=0)

	class Meta:
		verbose_name_plural = "Dishes"

	def __str__(self):
		return self.name

class Customer(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)

	orders = models.ManyToManyField('order')

	def __str__(self):
		return self.first_name + " " + self.last_name


class Order(models.Model):
	number = models.IntegerField(default=0)
	dishes = models.ManyToManyField('dish')

	date = models.DateTimeField(auto_now_add=True,)

	def total(self):
		log = []
		prices = []
		try:
			for i in self.dishes.all():
				prices.append(float(i.cost))

			total = sum(prices)
		except Exception as e:
			log.append(str(e))
		return total

	def order_number(self):
		try:
			total = self.id
		except:
			total = 20
		self.number = total
		self.save()
		return total

	def __str__(self):
		return str(self.order_number())