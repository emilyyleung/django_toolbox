from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from list_difference.forms import ListCheckerForm

def home(request):
    return JsonResponse({"app":"List checker"})

################################################################################

def check_list_difference(listA, listB):
	return list(set(listA) - set(listB))

def check_list_intersection(listA, listB):
	return list(set(listA) & set(listB))

def splitListToItems(inputList, listToAppend):
    clean_list = inputList.split(",")
    all_items = [x for x in clean_list if x]
    for i in all_items:
        x = i.replace("\r\n", "")
        x = i.strip()
        # x = x.replace("K:", prefix)
        listToAppend.append(x)
    return listToAppend

def sepComma(request):
	print("FORM")

	if request.method == 'POST':
		listForm = ListCheckerForm(request.POST)

		if listForm.is_valid():
			clean_listA = listForm.cleaned_data['listA'].strip()
			clean_listB = listForm.cleaned_data['listB'].strip()

			# multiline_list = []
			# multiline_input = listForm.cleaned_data['multiline']
			# multiline_list.append(multiline_input)
			# multiline_array = multiline_list[0].split("\r\n")
			# print(multiline_array)

			out = {}

			list_A = []
			list_B = []

			try:
				if "," in clean_listA:
					splitListToItems(clean_listA, list_A)
					splitListToItems(clean_listB, list_B)

					seen_A = {}
					dupes_A = []

					for x in list_A:
						if x not in seen_A:
							seen_A[x] = 1
						else:
							if seen_A[x] == 1:
								dupes_A.append(x)
							seen_A[x] += 1

					seen_B = {}
					dupes_B = []

					for x in list_B:
						if x not in seen_B:
							seen_B[x] = 1
						else:
							if seen_B[x] == 1:
								dupes_B.append(x)
							seen_B[x] += 1

					out["AB"] = check_list_difference(list_A, list_B)
					out["BA"] = check_list_difference(list_B, list_A)
					out["INTAB"] = check_list_intersection(list_A, list_B)
					out["DUPES_A"] = dupes_A
					out["DUPES_B"] = dupes_B

				return render(request, "list_difference/form_list.html", {"form": listForm, "out": out})

			except Exception as e:
				print(e)

			# print(list_A)
			# print(list_B)

	else:
		listForm = ListCheckerForm()
	return render(request, "list_difference/form_list.html", {"form": listForm})

def sepMulti(request):
	print("FORM")

	if request.method == 'POST':
		listForm = ListCheckerForm(request.POST)

		if listForm.is_valid():
			clean_listA = listForm.cleaned_data['listA'].strip()
			clean_listB = listForm.cleaned_data['listB'].strip()

			multiline_list_A = []
			multiline_list_B = []

			multiline_input_A = listForm.cleaned_data['listA']
			multiline_input_B = listForm.cleaned_data['listB']
			
			multiline_list_A.append(multiline_input_A)
			multiline_list_B.append(multiline_input_B)

			multiline_array_A = multiline_list_A[0].split("\r\n")
			multiline_array_B = multiline_list_B[0].split("\r\n")

			print(multiline_array_A)
			print(multiline_array_B)

			out = {}

			try:

				seen_A = {}
				dupes_A = []

				for x in multiline_array_A:
					if x not in seen_A:
						seen_A[x] = 1
					else:
						if seen_A[x] == 1:
							dupes_A.append(x)
						seen_A[x] += 1

				seen_B = {}
				dupes_B = []

				for x in multiline_array_B:
					if x not in seen_B:
						seen_B[x] = 1
					else:
						if seen_B[x] == 1:
							dupes_B.append(x)
						seen_B[x] += 1

				out["AB"] = check_list_difference(multiline_array_A, multiline_array_B)
				out["BA"] = check_list_difference(multiline_array_B, multiline_array_A)
				out["INTAB"] = check_list_intersection(multiline_array_A, multiline_array_B)
				out["DUPES_A"] = dupes_A
				out["DUPES_B"] = dupes_B

				separator = "\n"
				join = []
				joined = separator.join(check_list_difference(multiline_array_A, multiline_array_B))

				join.append(joined)

				print(join)

				out["ABC"] = join[0]

				return render(request, "list_difference/form_list.html", {"form": listForm, "out": out})

			except Exception as e:
				print(e)

			# print(list_A)
			# print(list_B)

	else:
		listForm = ListCheckerForm()
	return render(request, "list_difference/form_list.html", {"form": listForm})

def sepTextarea(request):
	print("FORM")

	if request.method == 'POST':
		listForm = ListCheckerForm(request.POST)

		if listForm.is_valid():
			clean_listA = listForm.cleaned_data['listA'].strip()
			clean_listB = listForm.cleaned_data['listB'].strip()

			multiline_list_A = []
			multiline_list_B = []

			multiline_input_A = listForm.cleaned_data['listA']
			multiline_input_B = listForm.cleaned_data['listB']
			
			multiline_list_A.append(multiline_input_A)
			multiline_list_B.append(multiline_input_B)

			multiline_array_A = multiline_list_A[0].split("\r\n")
			multiline_array_B = multiline_list_B[0].split("\r\n")

			print(multiline_array_A)
			print(multiline_array_B)

			unique_set = list(set(multiline_array_A + multiline_array_B))

			out = {}

			try:

				seen_A = {}
				dupes_A = []

				for x in multiline_array_A:
					if x not in seen_A:
						seen_A[x] = 1
					else:
						if seen_A[x] == 1:
							dupes_A.append(x)
						seen_A[x] += 1

				seen_B = {}
				dupes_B = []

				for x in multiline_array_B:
					if x not in seen_B:
						seen_B[x] = 1
					else:
						if seen_B[x] == 1:
							dupes_B.append(x)
						seen_B[x] += 1

				just_A = check_list_difference(multiline_array_A, multiline_array_B)
				just_B = check_list_difference(multiline_array_B, multiline_array_A)
				int_AB = check_list_intersection(multiline_array_A, multiline_array_B)

				just_A.sort()
				just_B.sort()
				int_AB.sort()
				dupes_A.sort()
				dupes_B.sort()
				unique_set.sort()			

				separator = "\n"
				multi_A = separator.join(just_A)
				multi_B = separator.join(just_B)
				multi_AB = separator.join(int_AB)
				multi_Dup_A = separator.join(dupes_A)
				multi_Dup_B = separator.join(dupes_B)
				multi_Set_AB = separator.join(unique_set)

				out["A_Only"] = multi_A
				out["B_Only"] = multi_B
				out["A_B"] = multi_AB
				out["Dup_A"] = multi_Dup_A
				out["Dup_B"] = multi_Dup_B
				out["Set_AB"] = multi_Set_AB

				return render(request, "list_difference/form_custom_textarea.html", {"form": listForm, "out": out})

			except Exception as e:
				print(e)

			# print(list_A)
			# print(list_B)

	else:
		listForm = ListCheckerForm()
	return render(request, "list_difference/form_custom_textarea.html", {"form": listForm})