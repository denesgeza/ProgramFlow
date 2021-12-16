def fizz_buzz(prompt = int) -> str:
    """fizz_buzz FizzBuzz game
    :param prompt: User input, defaults to int
    :param answer: Program output, defaults to str
    :rtype: str
    """
    if prompt % 15 == 0:
        return "fizz buzz"
    elif prompt % 3 == 0:
        return "fizz"
    elif prompt % 5 == 0:
        return 'buzz'
    else:
        return str(prompt)


input("Play Fizz Buzz.    Press ENTER to start!")
input()

next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = input("Your go: ")
    if players_answer != correct_answer:
        print("You lose, the correct answer was {}".format(correct_answer))
        break
else:
    print("Well done, you reached {}".format(next_number))

