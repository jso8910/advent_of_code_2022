from itertools import combinations


def get_input():
    with open("day_17/input.txt", "r") as f:
        file = f.read().splitlines()

    return list(map(int, file))


def part_one(containers):
    count_150 = 0
    combs = []
    for i in range(len(containers)):
        els = [list(x) for x in combinations(containers, i)]
        combs.extend(els)

    for comb in combs:
        if sum(comb) == 150:
            count_150 += 1

    return count_150


def part_two(containers):
    containers_lens = []
    combs = []
    for i in range(len(containers)):
        els = [list(x) for x in combinations(containers, i)]
        combs.extend(els)

    for comb in combs:
        if sum(comb) == 150:
            containers_lens.append(len(comb))

    return containers_lens.count(min(containers_lens))


print(part_one(get_input()))
print(part_two(get_input()))
