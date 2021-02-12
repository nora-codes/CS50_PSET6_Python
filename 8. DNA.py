# matching a sequance of DNA to an individual

import sys
import csv


def main():

    # Ensure correct usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # open CSV file using open function
    people = open_csv()

    # open txt file using DNA function and store as string DNA
    DNA = open_txt()

    # find STRS
    STRs = find_STR()

    # define list of STR strings
    STR = []

    # define list of STR max values
    STR_max = []

    # iterate through STRs
    for x in range(len(STRs)):

        # define STR string
        STR[len(STR):] = [STRs[x]]

        # find max number of repeats for STR
        STR_max[len(STR_max):] = [repeats(DNA, STR[x])]

    # iterate through people
    for y in range(len(people)):

        # define STR match counter and set to 0
        STR_match = 0

        # iterate through STRs
        for z in range(1, len(STRs)):

            # if match is found
            if int(people[y][STR[z]]) == STR_max[z]:

                # add +1 to the STR match counter
                STR_match += 1

           # if match is not found
            else:

                # break out of loop
                break

        # if all STRs are matched
        if STR_match == (len(STRs) - 1):

            # match is found - print name
            print(people[y]["name"])

            return

    # if no match is found
    print("No match")


# open the csv file and store contents to memory
def open_csv():

    # define list 'people'
    people = []

    # access and define filename for csv file with argv
    filename = sys.argv[1]

    # open and define csv file with filename
    with open(filename) as file:

        # read csv file
        # store content rows as dictionaries for each person
        reader = csv.DictReader(file)

        # iterate through rows in file
        for row in reader:

            # store each dictionary in list 'people'
            people[len(people):] = [row]

    return people


# open the csv file and find STRs listed
def find_STR():

    # define list 'STRs'
    STRs = []

    # access and define filename for csv file with argv
    filename = sys.argv[1]

    # open and define csv file with filename
    with open(filename) as file:

        # read csv file
        reader = csv.reader(file)

        # store first row in STRs list
        STRs = next(reader)

    return STRs


# open the txt file and store contents to memory
def open_txt():

    # define list 'sequence'
    sequence = []

    # access and define filename for txt file with argv
    filename = sys.argv[2]

    # open and define txt file with filename
    with open(filename) as file:

        # store file contents as string 'dna'
        dna = file.read()

    # return dna to main
    return dna


# returns the maximum number of times that the STR repeats in a DNA sequence
def repeats(DNA, STR):

    # define list to store number of STR repeats
    repeats = []

    # iterate through each position in DNA sequence
    for x in range(len(DNA)):

        # define y as the end of a substring
        y = x + len(STR)

        # set repeat counter to 0
        counter = 0

        # create a substring and check for match with STR
        while split(DNA, x, y) == STR:

            # if match is found add +1 to the repeat counter
            counter += 1

            # set beginning of substring to next position
            x = y

            # set end of substring to next position
            y = x + len(STR)

        # if repeat is found
        if counter > 0:

            # log repeat in repeats list
            repeats[len(repeats):] = [counter]

    # if STR has been found in sequence
    if len(repeats) > 0:

        # find maximum number of repeats in repeat list
        repeat_max = max(repeats)

        return repeat_max

    else:

        return 0


# split a substring from DNA sequence
def split(DNA, x, y):

    # define location of substring in DNA sequence
    substring = DNA[x:y]

    return substring


if __name__ == "__main__":
    main()
