from itertools import permutations, combinations
from math import inf, prod
from tqdm import tqdm


def get_input():
    with open("day_24/input.txt") as f:
        return [int(line) for line in f]


def part_one(weights):
    assert int(sum(weights) / 3) == sum(weights) / 3

    # This is guaranteed to work because min_first_group_size has to be <= len(weights) / 3
    min_first_group_size = len(weights) // 3 + 1
    min_qe = inf
    current_group_size = min_first_group_size
    while current_group_size > 0:
        if min_qe == 0:
            print(min_first_group_size, current_group_size, min_qe, "\n")
        for comb in combinations(weights, len(weights) if current_group_size > len(weights) else current_group_size):
            if sum(comb) == sum(weights) / 3 and len(comb) <= min_first_group_size:
                if len(comb) == min_first_group_size:
                    min_qe = min(min_qe, prod(comb))
                else:
                    min_qe = prod(comb)
                min_first_group_size = min(min_first_group_size, len(comb))
                break
        current_group_size -= 1

    return min_qe


def part_two(weights):
    assert int(sum(weights) / 4) == sum(weights) / 4

    # This is guaranteed to work because min_first_group_size has to be <= len(weights) / 4
    min_first_group_size = len(weights) // 4 + 1
    min_qe = inf
    current_group_size = min_first_group_size
    while current_group_size > 0:
        if min_qe == 0:
            print(min_first_group_size, current_group_size, min_qe, "\n")
        for comb in combinations(weights, len(weights) if current_group_size > len(weights) else current_group_size):
            if sum(comb) == sum(weights) / 4 and len(comb) <= min_first_group_size:
                if len(comb) == min_first_group_size:
                    min_qe = min(min_qe, prod(comb))
                else:
                    min_qe = prod(comb)
                min_first_group_size = min(min_first_group_size, len(comb))
                break
        current_group_size -= 1

    return min_qe


print(part_one(get_input()))
print(part_two(get_input()))
