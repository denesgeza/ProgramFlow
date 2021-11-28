numbers = input("Please enter 3 numbers separated by ,: ")

values = numbers.split(",")

integer_values =[]
for value in values:
    integer_values.append(int(value))

a = integer_values[0]
b = integer_values[1]
c = integer_values[2]

result = a + b - c
print(result)

