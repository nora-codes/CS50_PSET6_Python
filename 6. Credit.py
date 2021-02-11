# check credit card number

import cs50

# define card number 'n' and prompt input from user
n = cs50.get_string("Number: ")

# define length of card number
length = len(n)

# seperate digits into list
digit = list(n)

# define counter and set to 0
counter = 0

# Check validity with Luhn's algorithm:

# traverse through every other digit, starting with the number’s second-to-last digit
for x in range(length - 2, -1, -2):

    # define each digit 'd' then convert to integer and multiply by 2
    d = int(digit[x]) * 2

    # if d has double digits
    if d > 9:

        # create a list of digits 'y'
        y = list(str(d))

        # sum the two digits
        d = int(y[0]) + int(y[1])

    # add digit d to counter
    counter += d

# traverse through the digits that weren’t multiplied by 2 (starting from the end)
for x in range(length - 1, -1, -2):

    # define each digit 'd'
    d = int(digit[x])

    # add digit d to counter
    counter += d

# seperate digits of final counter value into list
count = list(str(counter))

# find length of final counter value
count_length = len(count)

# check to see if the last digit is 0
if not count[count_length - 1] == "0":

    # if card has failed Luhn's algorithm - return 'invalid'
    print("INVALID")

# check for length of 16 digits
elif length == 16:

    # check first two digits
    if digit[0] == "5" and int(digit[1]) > 0 and int(digit[1]) < 6:

        # comfirmed Mastercard
        print("MASTERCARD")

    # check first digit
    elif digit[0] == "4":

        # comfirmed Visa
        print("VISA")

# check for length of 15 digits and first two digits
elif length == 15 and digit[0] == "3" and (digit[1] == "4" or digit[1] == "7"):

    # comfirmed American Express
    print("AMEX")

# check for length of 13 digits and first digit
elif length == 13 and digit[0] == "4":

    # comfirmed Visa
    print("VISA")


else:
    # no valid credit card found
    print("INVALID")
