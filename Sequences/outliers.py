data = [4, 5, 6, 7, 7, 6, 56, 67, 43,
		140, 456, 457, 500]
print(len(data)) #just to understand the code easier;
print(range(len(data) - 1, -1, -1))
 
min_valid = 100
max_valid = 200

# process the lower values first
stop = 0
for index, value in enumerate(data):
	if value >= min_valid:
		stop = index
		break

print(stop)  # for debugging
del data[:stop]
print(data)
# process the high values in the list
start = 0
for index in range(len(data) - 1, -1, -1):
	if data[index] <= max_valid:
		#We jave the index of the last item to keep.
		#Set 'start' to the position of the first item to delete, which is 1 after 'index'.
		start = index + 1
		break
print(start) # for debugging
del data[start:]
print(data)
