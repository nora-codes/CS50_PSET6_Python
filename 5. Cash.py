import cs50

# define change owed and set to negative number
c = -1

# define coin counter and set to 0
n = 0

# check for non-negative value from user
while c < 0:

    # prompt user for change value
    c = cs50.get_float("Changed owed: ")

# return as many quarters (25¢) as possible
while c >= 0.25:
    c = round((c - 0.25), 2)
    n += 1

# return as many dimes (10¢) as possible
while c >= 0.1:
    c = round((c - 0.1), 2)
    n += 1

# return as many nickels (5¢) as possible
while c >= 0.05:
    c = round((c - 0.05), 2)
    n += 1

# return as many pennies (1¢) as possible
while c >= 0.01:
    c = round((c - 0.01), 2)
    n += 1

# print the minimum number of coins with which given change can be made
print(n)
