# Simulate a sports tournament

import csv
import sys
import random
import math

# Number of simluations to run
N = 1000


def main():

    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    # define list 'teams'
    teams = []

    # access and define filename with argv
    filename = sys.argv[1]

    # open and define file with filename
    with open(filename) as file:

        # read file and store content rows as dictionaries
        reader = csv.DictReader(file)

        # iterate through rows in file
        for row in reader:

            # convert rating to int
            row["rating"] = int(row["rating"])

            # store each dictionary list 'teams'
            teams[len(teams):] = [row]

    # define dictionary 'counts'
    counts = {}

    # run simulation 'N' times
    for x in range(N):

        # on simulation 'x' find winner of tournament
        winner = simulate_tournament(teams)

        # if team already exists in counts dictionary
        if winner in counts:

            # add +1 to tehir count
            counts[winner] += 1

        # if team does not exist in counts dictionary
        else:

            # create new dictionary value for team and set to 1 count
            counts[winner] = 1

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""

    # find winners of current round
    winners = simulate_round(teams)

    # if it is not the final round
    if len(winners) > 1:

        # return winners of next round
        return simulate_tournament(winners)

    # if it is the final round
    else:

        # return the name of the winning team
        return winners[0]["team"]


if __name__ == "__main__":
    main()
