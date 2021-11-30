from contents import pantry, recipes

#code from below will be learned later
#display_dict = {str(index +1): meal for index, meal in enumerate(recipes)}

display_dict = {}
for index, key in enumerate(recipes):
	# print(index, key)
	display_dict[str(index + 1)] = key

while True:
	# Display a menu of the recipes we know how to cook
	print("Please chose your recipe?")
	print("-------------------------")
	for key, value in display_dict.items():
		print(f"{key} - {value}")
	print('0 - to Exit')
	choice = input(": ")

	if choice == 0:
		break
	elif choice in display_dict:
		selected_item = display_dict[choice]
		print(f"You have selected: || {selected_item} ||")
		print("Checking ingredients ...")
		print()
		ingredients = recipes[selected_item]
		print(ingredients)

		for food_item in ingredients:
			if food_item in pantry:
				print(f'\t{food_item} OK')
			else:
				print(f"\tYou don't have the necessary ingredients.")


