# a program that computes the approximate grade level
# needed to comprehend some text

import cs50
import string
import math
import re

# ----- INPUT -----

# ask the user to type in some text
text = cs50.get_string("Text: ")

# define length of text
length = len(text)


# ----- WORDS -----

# split text into list of words
word = text.split(' ')

# define number of words
words = len(word)


# --- LETTERS ---

# split text into list of characters
character = list(text)

# define number of letters and set to 0
letters = 0

# iterate over characters in text
for x in range(length):

    # if an alphabet letter is found
    if character[x].isalpha() == True:

        # add +1 to 'letters' counter
        letters += 1

# define value L as per the Coleman-Liau index
L = (100 / words) * letters


# -- SENTENCES --

# split text into list of sentences
# (\ are used to escape RegEx metacharacters)
sentence = re.split('! |\. |\? |\n', text)

# define number of sentences
sentences = len(sentence)

# define value S as per the Coleman-Liau index
S = (100 / words) * sentences


# ---- INDEX ----

# calculate index and round to nearest whole number
index = round(0.0588 * L - 0.296 * S - 15.8)

# for high grades
if index >= 16:
    print("Grade 16+")

# for low grades
elif index < 1:
    print("Before Grade 1")

# for all other grades
else:
    print("Grade ", + index)
