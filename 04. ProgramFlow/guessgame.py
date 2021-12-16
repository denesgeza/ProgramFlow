answer = 5

print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess != answer:
    if guess < answer:
        print('Please guess higher')
    else: 
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print('Well done you guessed it!')
    else:
        print("Sorry, you have not guessed it!")
else:
    print("You've got it the first time!")
    
    
# if guess < answer:
#     print('Please guess higher!')
#     guess = int(input())
#     if guess == answer:
#         print("Well done you guesssed it!!")
#     else:
#         print("Sorry you didn't guessed it!")
# elif guess > answer:
#     print('Please guess lower!')
#     guess = int(input())
#     if guess == answer:
#         print("Well done you guesssed it!!")
#     else:
#         print("Sorry you didn't guessed it!")
# else: 
#     print('You got it!')