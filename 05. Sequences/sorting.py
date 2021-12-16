pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
print(letters)

numbers = [2.3, 4.5, 8.7, 9.3, 1.6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

numbers.sort()
print(numbers)

sorting_literals = sorted("The quick brown fox jumps")
print(sorting_literals)

# to sort case-Insesitive --> add key = str.casefold
sorting_literals = sorted("The quick brown fox jumps",
						  key=str.casefold)
print(sorting_literals)

names = ['Graham',
		 'John',
		 'terry',
		 'Marco',
		 'pistike'
		 ]
names.sort(key=str.casefold)
print(names)



# NOTES:
# using the sorted command we create a new list
# we have 2 lists: numbers and sorted_numbers
# using the .sort() method we sort the same list
#