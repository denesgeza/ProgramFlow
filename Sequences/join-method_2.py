flowers = [
	'lavender',
	'tiger lily',
	'iris',
	'sunflower',
]

# for flower in flowers:
# 	print(flower)

separator = ' || '
output = separator.join(flowers)
print(output)

print(", ".join(flowers))

#NOTES
# each of the item is joined into a single string and separated by a  " | "
# all items MUST be str
# if int an str are mixed the code crashes
