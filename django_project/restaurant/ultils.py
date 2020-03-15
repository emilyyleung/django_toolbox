def get_default_course(model):
	# return Course.objects.first()
	test = model.objects.get(course_name="N/A")
	return test.id