def largest(list):
	largest = list[0]
	for i in list:
		if i>largest:
			largest=i
	return largest
list=[45,56,98,3,67,9,90]
print("Largest number is",largest(list))    


