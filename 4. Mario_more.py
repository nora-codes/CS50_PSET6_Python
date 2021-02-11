# Mario_less

import cs50

# define height and set to 0
h = 0

# check for correct input - reprompt if necessary
while h < 1 or h > 8:
    h = cs50.get_int("Height: ")


# generate half-pyramid
for x in range(h):
    i = x + 1
    for a in range(h - i):
        print(" ", end="")
    for b in range(i):
        print("#", end="")
    print("  ", end="")
    for c in range(i):
        print("#", end="")
    print("")
