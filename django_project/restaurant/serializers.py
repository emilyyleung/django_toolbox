from rest_framework import serializers
from . models import *


class DishSerializer(serializers.ModelSerializer):
	class Meta:
		model = Dish
		# fields = ['name', 'description', 'cost', 'vegan']
		fields = ('__all__')