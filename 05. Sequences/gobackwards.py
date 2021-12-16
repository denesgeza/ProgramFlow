data = [104, 101, 4, 105, 308, 103, 5,
		107, 100, 306, 106, 102, 108, 306]

min_valid = 100
max_valid = 200
# option 1 - iterating backwards
# for index in range((len(data) - 1), -1, -1):
# 	if data[index] < min_valid or data[index] > max_valid:
# 		#print(index, data) #debugging purposes only
# # 		del data[index]
# print(data)

# option 2
# index location start the same from 0 onwards, but
# the list is reversed
top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
	if value < min_valid or value > max_valid:
		print(top_index - index, value) #debug only
		del data[top_index - index]
print(data)



#NOTE
# it's better to iterate backwards to not mess up the indexes
