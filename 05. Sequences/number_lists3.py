even = [2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9]

# add odd list to even
numbers = [even, odd]
print(numbers)

for number_list in numbers:
	print(number_list)

	for value in number_list:
		print(value)
