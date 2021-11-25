# code 1
# day = "Saturday"
# temperature = 30
# raining = True
#
# if (day == "Saturday" and temperature > 27) or not raining:
#     print('Go swimming')
# else:
#     print('Learn python')

if 0:
    print(True)
else:
    print(False)

name = input('Please enter your name: ')
# name can be left empty also, preferably write with !=
# if name:
if name != "":
    print('Hello, {}'.format(name))
else:
    print('Are yo u the man with no name?')