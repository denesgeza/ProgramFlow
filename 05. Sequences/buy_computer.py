current_choice = '-'
computer_parts = [] # create an empty list

while current_choice != '0':
	if current_choice in '12345':
		print('Adding {}'.format(current_choice))
		if current_choice == '1':
			computer_parts.append('monitor')
		elif current_choice == '2':
			computer_parts.append('keyboard')
		elif current_choice == '3':
			computer_parts.append('mouse')
		elif current_choice == '4':
			computer_parts.append('printer')
		elif current_choice == '5':
			computer_parts.append('cables')
	else:
		print('Please add options for your computer:')
		print('1: monitor')
		print('2: keyboard')
		print("3: mouse")
		print('4: printer')
		print('5: cables')
		print('0: to finish')

	current_choice = input()

print(computer_parts)