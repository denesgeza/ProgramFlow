import random


def get_integer(prompt):
    """
    Get an integer from Standard Input (stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered.

    :param prompt: The string the user will see, when
    they're prompted to enter a value.
    :return: The integer the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else:
        #     print('{0} is not a number'.format(temp))
        print('{0} is not a number'.format(temp))

#NOTES how to print the docstring
print(input.__doc__)
print("*" * 80)
print(get_integer.__doc__)
print('*' * 80)

help(get_integer)


HIGHEST = 1000
answer = random.randint(1, HIGHEST)
print(answer)  # TODO: Remove after testing.
guess = 0  # initialise to any number that doesn't equal answer
print("Please guess a number between 1 and {}: ".format(HIGHEST))

while guess != answer:
    guess = get_integer(': ')

    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:  # guess must be greater than answer
            print("Please guess lower")

# NOTES
# else is not required in the function if the print is indented out
# in case of using else the output should be the same
# NOTES Docstrings
