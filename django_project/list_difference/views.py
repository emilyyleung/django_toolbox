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

def form(request):
	print("FORM")

	if request.method == 'POST':
		listForm = ListCheckerForm(request.POST)

		if listForm.is_valid():
			clean_listA = listForm.cleaned_data['listA'].strip()
			clean_listB = listForm.cleaned_data['listB'].strip()

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

				return render(request, "list_difference/form.html", {"form": listForm, "out": out})

			except Exception as e:
				print(e)

			# print(list_A)
			# print(list_B)

	else:
		listForm = ListCheckerForm()
	return render(request, "list_difference/form.html", {"form": listForm})