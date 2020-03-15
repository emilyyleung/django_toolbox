from django import template
register = template.Library()

@register.filter
def createList(value):
	arr = []
	counter = 0
	while counter < value:
		arr.append("X")
		counter = counter + 1

	return arr
