# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i, i * j)


nested_data = [(i, i * j) for i in range(1, 11) for j in range(1, 11)]
# print(nested_data)

# for x, y in [(i, i * j) for i in range(1, 11) for j in range(1, 11)]:
    # print(x, y)

nested_data_2 = [[(i, i * j) for i in range(1, 11)] for j in range(1, 11)]
# print(nested_data_2)

for x, y in ((i, i * j) for i in range(1, 11) for j in range(1, 11)):
    print(x, y)