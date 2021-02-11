# Mario_less

import cs50

# define height and set to 0
h = 0

# check for correct input - reprompt if necessary
while h < 1 or h > 8:
    h = cs50.get_int("Height: ")


# generate half-pyramid
for x in range(h):
    for y in range(h - (x + 1)):
        print(" ", end="")
    for z in range(x + 1):
        print("#", end="")
    print("")
