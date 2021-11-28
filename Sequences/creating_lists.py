empty_list = []

even = [2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

digits = sorted('43234564573908')
print(digits)

digits = list('43234564573908')
print(digits)

#the list command creates a new list, it has the same items but different id
#more_numbers = list(numbers)
#more_numbers = numbers.copy()
more_numbers = numbers[:]
print(more_numbers)

print(numbers is more_numbers)
print(numbers == more_numbers)


# NOTES
# the sorted new list will have same type as the list to be sorted int or str