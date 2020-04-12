from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import SafeString
register = template.Library()

@register.filter
@stringfilter
def createEllipsis(value):
	string_max_length = 75;
	string_length = len(value)

	if string_length > string_max_length:
		new_string = value[:string_max_length] + "...";
	else:
		new_string = value

	# new_string = value

	return new_string

@register.filter
def createList(value):
	arr = []
	counter = 0
	while counter < value:
		arr.append("X")
		counter = counter + 1

	return arr

@register.filter
def objToString(value):
	return str(value)
