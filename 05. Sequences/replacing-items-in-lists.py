computer_parts = ['PC',
				  'monitor',
				  'keyboard',
				  'mouse',
				  'mouse pad',
				  ]

print(computer_parts)

# computer_parts[3] = 'trackball'
print(computer_parts[3:])

# the contents of the list from index 3 to end is replaced with trackball
# computer_parts[3:] = ['trackball']
# print(computer_parts)
# only the contents of index 3 is replaced
computer_parts[3:4] = ['trackball']
print(computer_parts)

computer_parts[3] = 'trackball'
print(computer_parts)
