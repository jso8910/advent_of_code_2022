from collections import defaultdict
from itertools import permutations
from math import inf


def get_input():
    with open("day_9/input.txt", "r") as f:
        file = f.read().splitlines()

    cities = set()
    edges = defaultdict(dict)
    for line in file:
        tokens = line.replace("to", "=").split(" = ")
        cities.add(tokens[0])
        cities.add(tokens[1])
        edges[tokens[0]][tokens[1]] = int(tokens[2])
        edges[tokens[1]][tokens[0]] = int(tokens[2])

    cities = list(cities)
    return edges, cities


def part_one(edges, cities):
    permutes = permutations(cities)
    dists = []
    for permutation in permutes:
        dist = sum(
            map(lambda start, end: edges[start][end], permutation, permutation[1:]))
        dists.append(dist)

    return min(dists)


def part_two(edges, cities):
    permutes = permutations(cities)
    dists = []
    for permutation in permutes:
        dist = sum(
            map(lambda start, end: edges[start][end], permutation, permutation[1:]))
        dists.append(dist)

    return max(dists)


print(part_one(*get_input()))
print(part_two(*get_input()))
