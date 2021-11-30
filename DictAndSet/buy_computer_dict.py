available_parts = {"1": 'monitor',
				   "2": 'keyboard',
				   "3": 'mouse',
				   "4": 'printer',
				   "5": 'cables',
				   "6": 'DVD drive',
				   '7': 'microphone',
				   }

current_choice = None
computer_parts = {}		# create an empty dict
# using in in a dict, is only checking the keys and not the values
while current_choice != "0":
	if current_choice in available_parts:
		chosen_part = available_parts[current_choice]
		if current_choice in computer_parts:
				# remove chosen_part
			computer_parts.pop(current_choice)
			print(f'Removing {chosen_part}')
		else:
			computer_parts[current_choice] = chosen_part
			print(f'Adding {chosen_part}')
		print(f"Your dictionary now contains: {computer_parts}")
	else:
		print("Please add options from the list")
		for key, value in available_parts.items():
			print(f"{key}: {value}")
		print("0: to finish")

	current_choice = input("> ")

print(computer_parts)
