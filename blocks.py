#how to create a code block
# block of code run separately
for i in range(1, 9):
    print('No.  {} square is {:3} and cubed is {:>4}'.format(i, i ** 2, i ** 3))
print('*' * 50)

# code run at the same time, check results
for i in range(1, 5):
    print('No.  {} square is {} and cubed is {:2}'.format(i, i ** 2, i ** 3))
    print('*' * 50)


    