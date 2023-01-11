import re
from itertools import combinations_with_replacement
from math import prod


def get_input():
    with open("day_15/input.txt", "r") as f:
        file = f.read().splitlines()

    prog = re.compile(
        r"(\b[a-zA-Z]+\b): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)")
    ingredients = []
    labels = ["capacity", "durability", "flavor", "texture", "calories"]
    for line in file:
        match = prog.match(line)
        if match:
            name = match.group(1)
            ingredients.append(
                [int(match.group(i)) for i in range(2, 7)])

    return ingredients


def part_one(ingredients):
    # permutes = product(ingredients.keys(), repeat=100)
    # print(len(list(permutes)))
    max_score = 0
    for comb in combinations_with_replacement(ingredients, 100):
        nums = [comb.count(ingredients[0]) * ingredients[0][i] +
                comb.count(ingredients[1]) * ingredients[1][i] +
                comb.count(ingredients[2]) * ingredients[2][i] +
                comb.count(ingredients[3]) * ingredients[3][i]
                for i in range(4)]
        if prod(nums) > max_score and all(i > 0 for i in nums[:4]):
            max_score = prod(nums)

    return max_score


def part_two(ingredients):
    # permutes = product(ingredients.keys(), repeat=100)
    # print(len(list(permutes)))
    max_score = 0
    for comb in combinations_with_replacement(ingredients, 100):
        nums = [comb.count(ingredients[0]) * ingredients[0][i] +
                comb.count(ingredients[1]) * ingredients[1][i] +
                comb.count(ingredients[2]) * ingredients[2][i] +
                comb.count(ingredients[3]) * ingredients[3][i]
                for i in range(4)]
        cals = comb.count(ingredients[0]) * ingredients[0][4] + \
            comb.count(ingredients[1]) * ingredients[1][4] + \
            comb.count(ingredients[2]) * ingredients[2][4] + \
            comb.count(ingredients[3]) * ingredients[3][4]
        if prod(nums) > max_score and all(i > 0 for i in nums[:4]) and cals == 500:
            max_score = prod(nums)

    return max_score


print(part_one(get_input()))
print(part_two(get_input()))
