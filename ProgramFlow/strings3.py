#         012345678901234
parrot = "Norwegian Blue"
# slicing put characters from strings
print(parrot[0:6])     # Norweg
print(parrot[-14:-8])  # Norweg

print(parrot[3:5])     # we
print(parrot[0:9])     # Norwegian
print(parrot[:9])      # Norwegian , first index can be skipped, because default = 0

print(parrot[10:])     # from index no 10 to end
print(parrot[10:14])    # if the index is the last index it includes the last value

print(parrot[:6])
print(parrot[6:])

print(parrot[:6] + parrot[6:])  # it prints the complete string

print(parrot[:])     #it prints the complete string

letters = 'abcdefghijklmnopqrstuvxyz'

print(letters[6:10])

print(parrot[-4:-2])    #Bl
print(parrot[-4:12])    #Bl

#Stepping in the slicing
print(parrot[0:6:2])   #  Nre Firstly it slices out char from 0 to 6 (not including 6) then steps into the second character
print(parrot[0:6:3])   # Nw  ,slice from 0 to 6 (not including 6) then steps into the 3rd character

number = '9,223;372:036,854,775,807'
print(number[1::4])     # , , , , , , , , 

number = '9,223;372:036 854,775;807'   
print(number[1::4])     #,;: ,;

separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])