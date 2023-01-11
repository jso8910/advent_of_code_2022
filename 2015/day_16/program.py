from collections import defaultdict

STATE = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}


def get_input():
    with open("day_16/input.txt", "r") as f:
        file = f.read().splitlines()

    sues = []
    for line in file:
        sue = defaultdict(lambda: None)
        line = ": ".join(line.split(": ")[1:])
        pairs = line.split(", ")
        for pair in pairs:
            sue[pair.split(": ")[0]] = int(pair.split(": ")[1])

        sues.append(sue)

    return sues


def part_one(sues):
    sue_answers = []
    for sue in sues:
        sue_answers.append(True)
        for key, value in sue.items():
            if value != STATE[key]:
                sue_answers[-1] = False

    return sue_answers.index(True) + 1


def part_two(sues):
    sue_answers = []
    for sue in sues:
        sue_answers.append(True)
        for key, value in sue.items():
            match key:
                case "cats" | "trees":
                    if value <= STATE[key]:
                        sue_answers[-1] = False
                case "pomeranians" | "goldfish":
                    if value >= STATE[key]:
                        sue_answers[-1] = False
                case _:
                    if value != STATE[key]:
                        sue_answers[-1] = False

    return sue_answers.index(True) + 1


print(part_one(get_input()))
print(part_two(get_input()))
