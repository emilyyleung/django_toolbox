import pytz

def allTimeZones():
	out = []
	alltimezones = pytz.all_timezones
	out = [(val, val) for val in alltimezones]
	return out
