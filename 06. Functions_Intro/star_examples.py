numbers = (0, 1, 2, 3, 4, 5)

# print(numbers, sep=";")     # the ";" is not used, without the *
# print(*numbers, sep=';')    # NOTES the "*" unpacks the numbers
# print(0, 1, 2, 3, 4, 5, sep=" ;")     # same as in here

def test_star(*args):
    print(args)
    for x in args:
        print(x)
        

test_star(0, 1, 2, 3, 4, 5)

print()

test_star()

# NOTES
# *args = represents an unpacked tuple
# args = represents a tuple