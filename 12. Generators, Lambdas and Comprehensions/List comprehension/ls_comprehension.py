print(__file__)

numbers = [1, 2, 3, 4, 5, 6]

squares_for_loop = []
for number in numbers:
    squares_for_loop.append(number ** 2)

squares_range = [number ** 2 for number in range(1, 7)]

squares_list_comprehension = [number ** 2 for number in numbers]
squares_set_comprehension = {number ** 2 for number in numbers}

print(squares_range)
print(squares_for_loop)
print(squares_list_comprehension)
print(squares_set_comprehension)

text = "what have the romans ever done for us"

capitals = [char.upper() for char in text]
print(capitals)

words = [word.upper() for word in text.split(' ')]
print(words)

lc_words = text.split(' ')
print(lc_words)