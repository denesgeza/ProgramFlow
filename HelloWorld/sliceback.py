#          01234567890123456789012345
letters = 'abcdefghijklmnopqrstuvwxyz'

# negative steps
backwards = letters[25:0:-1]    # zyxwvutsrqponmlkjihgfedcb
print(backwards)

backwards = letters[25::-1]    # zyxwvutsrqponmlkjihgfedcba
print(backwards)


backwards = letters[::-1]    # zyxwvutsrqponmlkjihgfedcba
print(backwards)

# qpo - slice the str to produce
backwards = letters[16:13:-1]
print(backwards)
# slice the str to produce edcba
backwards = letters[4::-1]
print(backwards)
# last 8 char in reverse order
backwards = letters[:-9:-1]     #zyxwvuts
print(backwards)

print(letters[-4:])     # last 4 letters
print(letters[-1:])     # last letter = "z"
print(letters[:1])      # first letter "a"
print(letters[0])       # a , if the str = " " is empty it doesnt execute

