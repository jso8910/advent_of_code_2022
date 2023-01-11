import re
from collections import defaultdict
from itertools import permutations


def get_input():
    with open("day_13/input.txt", "r") as f:
        file = f.read().splitlines()

    prog = re.compile(
        r"(\b[a-zA-Z]+\b) would (\b[a-zA-Z]+\b) (\d+) happiness units by sitting next to (\b[a-zA-Z]+\b)")
    people = defaultdict(dict)
    for line in file:
        match = prog.match(line)
        if match:
            name = match.group(1)
            name2 = match.group(4)
            if match.group(2) == "gain":
                people[name][name2] = int(match.group(3))
            else:
                people[name][name2] = -int(match.group(3))

    return people


def part_one(people):
    max_happiness = 0
    for seating in permutations(people.keys()):
        happiness = 0
        for i in zip(seating, seating[1:]):
            happiness += people[i[0]][i[1]] + people[i[1]][i[0]]

        # Don't forget the table is a circle
        happiness += people[seating[0]][seating[-1]] + \
            people[seating[-1]][seating[0]]

        if happiness > max_happiness:
            max_happiness = happiness

    return max_happiness


def part_two(people):
    max_happiness = 0
    people["me"] = {}
    for seating in permutations(people.keys()):
        happiness = 0
        for i in zip(seating, seating[1:]):
            if i[0] != "me" and i[1] != "me":
                happiness += people[i[0]][i[1]] + people[i[1]][i[0]]

        # Don't forget the table is a circle
        if seating[0] != "me" and seating[-1] != "me":
            happiness += people[seating[0]][seating[-1]] + \
                people[seating[-1]][seating[0]]

        if happiness > max_happiness:
            max_happiness = happiness

    return max_happiness


print(part_one(get_input()))
print(part_two(get_input()))
