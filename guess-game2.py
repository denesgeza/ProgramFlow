answer = 5

print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess == answer:
    print("You've got it the first time!")
else:
    if guess < answer:
        print('Please guess higher')
    else:
        print("Please guess lower")    
    guess = int(input())
    if guess == answer:
        print('Well done you guessed it!')
    else:
        print('Sorry, better luck next time')
