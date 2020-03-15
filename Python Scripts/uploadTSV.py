import csv
import json
import collections
import requests
import urllib

OrderedDict = collections.OrderedDict

src = 'DATABASE - MENU.tsv'
# src = 'DATABASE_ppl.tsv'
dst = 'data.json'

posturl = "http://localhost:8000/restaurant/uploadDishes/"
# posturl = "http://localhost:8000/restaurant/uploadCustomers/"

header = ['name', 'description', 'cost', 'vegan', 'vegetarian_option', 'gluten_free', 'signature_dish', 'spice_level', 'pieces', 'dish_course']
# header = ['first_name', 'last_name']

data = []

tsv_headers = []

def run1():
	with open(src, 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter='\t')
		for row in reader:
			tsv_headers.append(row)
			# print(row)

	tsv_parameters = []

	for h in tsv_headers[0]:
		tsv_parameters.append(h)

	print(tsv_parameters)

def run2():

	with open(src, 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter='\t')
		x = 0
		for row in reader:
			if x == 0:
				x += 1
				pass
			else:
				data.append(OrderedDict(zip(header, row)))

	json_data = json.dumps(data)

	new_data = json.loads(json_data)

	out = {
		"data": json.dumps(new_data)
	}

	# print(out)
	try:
		r = requests.post(posturl, out)
		# r = requests.get(url).json()
		job = r.json()
		print(job)
	except Exception as e:
		print(e)
	# postdata = []

	# for x in new_data:
	# 	topost = {
	# 		"data": json.dumps([x])
	# 	}
	# 	postdata.append(topost)

	# print(postdata)

	# for x in postdata:
	# 	r = requests.post(posturl, x)
	# 	job = r.json()
	# 	print(job)

	# with open(dst, 'w') as jsonfile:
	# 	json.dump(data, jsonfile, indent=2)

# run1()
run2()