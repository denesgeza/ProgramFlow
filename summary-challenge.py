print('Please choose from the list below: ')
print('1.\tLearn Python')
print('2.\tTake a break')
print('3.\tGet a new job')
print('4.\tQuit smokking')
print('0.\tExit')

choice = '-'
while choice == '0':
    if choice in '12345':
        print('You chose {}'.format(choice))
    else:
        print('Please choose from the list below: ')
        print('1.\tLearn Python')
        print('2.\tTake a break')
        print('3.\tGet a new job')
        print('4.\tQuit smokking')
        print('0.\tExit')




