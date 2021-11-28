available_parts = ['monitor',
				   'keyboard',
				   'mouse',
				   'printer',
				   'cables',
				   'DVD drive',
				   'microphone'
				   ]

valid_choices = []
for i in range(1, len(available_parts) + 1):
	# range equals list length + 1, and starts from 1
	valid_choices.append(str(i))
# convert valid choices to strings
print(valid_choices)
current_choice = '-'  # no assigned value currently
computer_parts = []  # create an empty list to be filled

while current_choice != '0':  # while user input != 0
	# user choice must be from the valid ones
	if current_choice in valid_choices:
		# print the current selection

		# the index is equal to the inputted integer value
		index = int(current_choice)  # convert to int
		# selected option equals to the index of the list
		chosen_parts = available_parts[index]
		# add selected parts to our new list
		if chosen_parts in computer_parts:
			#it's already in so remove it
			print('Removing {}'.format(chosen_parts))
			computer_parts.remove(chosen_parts)
		else:
			print('Adding {}'.format(chosen_parts))
			computer_parts.append(chosen_parts)
		print("Your list now contains: {}".format(computer_parts))
	else:
		print('Please add options for your computer:')
		# added a for loop to generate the list
		for number, part in enumerate(available_parts):
			# number is the index of the list and part is the object from the list
			print('{0}: {1}'.format(number + 1, part))  # print index + 1, because it starts with 0

	current_choice = input()

print(computer_parts)

# NOTES:
# use .append() to add to a list
# use .remove() to remove an item from a list
# using the .sort() method we sort the same list
