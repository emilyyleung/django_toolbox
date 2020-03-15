from rest_framework import serializers
from . models import *

class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		exclude = ('translation',)

class DishSerializer(serializers.ModelSerializer):
	dish_course = CourseSerializer()
	class Meta:
		model = Dish
		# fields = ['name', 'description', 'cost', 'vegan']
		fields = ('__all__')