from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import os
import json
import re

from jsonmaker.forms import BulkRenameForm, JsonMakerForm

# Create your views here.
def jsonhome(request):
	return HttpResponse('<h1>JSON MAKER</h1>')

def convert(request):

	data = "hello = world"

	return JsonResponse({"hello": "world"})

def compileJSON(current_filenames, new_filenames):
	pass

def bulkrename(request):
	print("FORM")

	if request.method == 'POST' and 'create' in request.POST:
		print("CREATE TABLE")
		jsonForm = BulkRenameForm(request.POST)

		if jsonForm.is_valid():
			clean_currentFileNames = jsonForm.cleaned_data['listA']
			clean_newFileNames = jsonForm.cleaned_data['listB']

			multiline_list_A = []
			multiline_list_B = []

			multiline_list_A.append(clean_currentFileNames)
			multiline_list_B.append(clean_newFileNames)

			string_A = multiline_list_A[0]
			string_B = multiline_list_B[0]

			multiline_array_A = re.findall(r"\b.+\b", string_A)

			multiline_array_A_clean = []

			for i in multiline_array_A:
				replace_space = i.replace(u'\xa0', u' ')
				print(replace_space)
				multiline_array_A_clean.append(replace_space)

			multiline_array_B = re.findall(r"\b.+\b", string_B)

			print(multiline_array_A_clean)
			print(multiline_array_B)

			filenames = []

			for old, new in zip(multiline_array_A_clean, multiline_array_B):
				obj = {}
				obj["old"] = old
				obj["new"] = new

				filenames.append(obj)

			print(filenames)

			return render(request, "jsonmaker/form.html", {"form": jsonForm, "filenames": filenames})

	elif request.method == 'POST' and 'rename' in request.POST:
		jsonForm = BulkRenameForm(request.POST)
		print("RENAME FILES")
		if jsonForm.is_valid():

			inputpath = jsonForm.cleaned_data['directory'].strip()

			clean_currentFileNames = jsonForm.cleaned_data['listA']
			clean_newFileNames = jsonForm.cleaned_data['listB']

			# ----------------------------------------------

			multiline_list_A = []
			multiline_list_B = []

			multiline_list_A.append(clean_currentFileNames)
			multiline_list_B.append(clean_newFileNames)

			string_A = multiline_list_A[0]
			string_B = multiline_list_B[0]

			multiline_array_A = re.findall(r"\b.+\b", string_A)

			multiline_array_A_clean = []

			for i in multiline_array_A:
				replace_space = i.replace(u'\xa0', u' ')
				multiline_array_A_clean.append(replace_space)

			multiline_array_B = re.findall(r"\b.+\b", string_B)

			print(multiline_array_A_clean)
			print(multiline_array_B)

			arr_filenames = []

			for old, new in zip(multiline_array_A_clean, multiline_array_B):
				obj = {}
				obj["old"] = old
				obj["new"] = new

				arr_filenames.append(obj)

			print(arr_filenames)

			# ----------------------------------------------
			try:
				enterpath = os.chdir(inputpath)

				filenames = os.listdir(enterpath)

			except Exception as e:
				return render(request, "jsonmaker/form.html", {"form": jsonForm, "filenames": arr_filenames, "working": "FALSE", "error": str(e)})

			try:
				for filename in filenames:
					
					# For each of the rename dictionaries
					for i in arr_filenames:
						
			   			# If the filename includes any of the "old" values
						if i["old"] in filename:
							
								print(filename + "|" + i["new"])

								newName = i["new"].split(".")
								del newName[-1]
								joinNewName = "".join(newName)

								splitName = filename.split(".")
								del splitName[-1]

								joinSplitName = "".join(splitName)

				   				# Creates new file name
								newFilename = filename.replace(joinSplitName, joinNewName)

								# Updates the current file name with the new file name
								os.rename(filename, newFilename)

				return render(request, "jsonmaker/form.html", {"form": jsonForm, "filenames": arr_filenames, "working": "TRUE"})

			except Exception as e:
				return render(request, "jsonmaker/form.html", {"form": jsonForm, "filenames": arr_filenames, "working": "FALSE", "error": str(e)})

	else:
		jsonForm = BulkRenameForm()
		
	return render(request, "jsonmaker/form.html", {"form": jsonForm})

def jsonmake(request):
	print("FORM")

	if request.method == 'POST' and 'create' in request.POST:
		print("CREATE TABLE")
		jsonForm = JsonMakerForm(request.POST)

		if jsonForm.is_valid():
			clean_currentFileNames = jsonForm.cleaned_data['listA']
			clean_newFileNames = jsonForm.cleaned_data['listB']

			multiline_list_A = []
			multiline_list_B = []

			multiline_list_A.append(clean_currentFileNames)
			multiline_list_B.append(clean_newFileNames)

			string_A = multiline_list_A[0]
			string_B = multiline_list_B[0]

			multiline_array_A = re.findall(r"\b.+\b", string_A)

			multiline_array_B = re.findall(r"\b.+\b", string_B)

			print(multiline_array_A)
			print(multiline_array_B)

			dictionary = {}
			for key, value in zip(multiline_array_A, multiline_array_B):
				obj = {}
				try:
					obj[key] = int(value)
				except:
					obj[key] = value
				dictionary.update(obj)

			print(dictionary)

			return render(request, "jsonmaker/jsonmaker.html", {"form": jsonForm, "working":"TRUE", "dictionary": json.dumps(dictionary), "pretty_dictionary": json.dumps(dictionary, indent=4, sort_keys=True)})
	else:
		jsonForm = JsonMakerForm()
		
	return render(request, "jsonmaker/jsonmaker.html", {"form": jsonForm})