from collections import defaultdict
import math


def get_input():
    with open("day_17/input.txt", "r") as f:
        file = f.read()

    transformations = []
    RIGHT = 1
    LEFT = -1

    for char in file:
        if char == ">":
            transformations.append(RIGHT)
        else:
            transformations.append(LEFT)

    return transformations


ROCKS = [
    [
        [True, True, True, True]
    ],
    [
        [False, True, False],
        [True, True, True],
        [False, True, False]
    ],
    [
        [False, False, True],
        [False, False, True],
        [True, True, True]
    ],
    [
        [True],
        [True],
        [True],
        [True]
    ],
    [
        [True, True],
        [True, True]
    ]
]


def part_one(transformations):
    # 7 units wide, -1j is down, +1j is up
    NUM_ROCKS = 2022
    chamber = set()
    current_rock = 0
    highest_rock = -1
    transformations_idx = 0
    for i in range(NUM_ROCKS):
        rock = ROCKS[i % len(ROCKS)]
        left_edge = 2
        bottom = highest_rock + 3 + 1

        current_rock_loc = set()
        for idx, row in enumerate(rock[::-1]):
            for c_idx, col in enumerate(row):
                if col:
                    current_rock_loc.add(left_edge + c_idx +
                                         (bottom + idx)*1j)
        # print(current_rock_loc)
        it_num = 0
        while True:
            if it_num % 2 == 0:
                # Get moved by jet
                transformation = transformations[transformations_idx % len(
                    transformations)]
                new_rock = {
                    coord + transformation for coord in current_rock_loc}
                if not new_rock & chamber and not {r.real for r in new_rock} & {-1, 7}:
                    current_rock_loc = new_rock
                transformations_idx += 1
            else:
                new_rock = {
                    coord - 1j for coord in current_rock_loc}
                if not new_rock & chamber and not {r.imag for r in new_rock} & {-1}:
                    current_rock_loc = new_rock
                else:
                    chamber |= current_rock_loc
                    break
            it_num += 1
        # print(chamber)
        highest_rock = int(max([c.imag for c in chamber]))

    return highest_rock + 1


def part_two(transformations):
    cache = {}
    NUM_ROCKS = 1_000_000_000_000
    chamber = set()
    current_rock = 0
    highest_rock = -1
    transformations_idx = 0
    i = 0

    for i in range(NUM_ROCKS):
        delta_max_height_by_col = [
            int(highest_rock - max([c.imag for c in chamber if c.real == col] + [0])) for col in range(7)]

        # The key in the cache is this: "<current rock idx><current transformation idx><height of highest rock - height of column for column in columns>"
        if not f"{i % len(ROCKS)}{transformations_idx % len(transformations)}{''.join(str(n) for n in delta_max_height_by_col)}" in cache:
            cache[f"{i % len(ROCKS)}{transformations_idx % len(transformations)}{''.join(str(n) for n in delta_max_height_by_col)}"] = (
                i, highest_rock)
        else:
            period = i - \
                cache[f"{i % len(ROCKS)}{transformations_idx % len(transformations)}{''.join(str(n) for n in delta_max_height_by_col)}"][0]
            change_over_period = highest_rock - \
                cache[f"{i % len(ROCKS)}{transformations_idx % len(transformations)}{''.join(str(n) for n in delta_max_height_by_col)}"][1]
            num_periods_left, rem = divmod((NUM_ROCKS - i), period)
            if not rem:     # If the number of periods left is exact, we're done!
                # Don't forget that you need to add 1 to highest_rock
                return (highest_rock + 1) + change_over_period * num_periods_left

        rock = ROCKS[i % len(ROCKS)]
        left_edge = 2
        bottom = highest_rock + 3 + 1

        current_rock_loc = set()
        for idx, row in enumerate(rock[::-1]):
            for c_idx, col in enumerate(row):
                if col:
                    current_rock_loc.add(left_edge + c_idx +
                                         (bottom + idx)*1j)
        # print(current_rock_loc)
        it_num = 0
        while True:
            if it_num % 2 == 0:
                # Get moved by jet
                transformation = transformations[transformations_idx % len(
                    transformations)]
                new_rock = {
                    coord + transformation for coord in current_rock_loc}
                if not new_rock & chamber and not {r.real for r in new_rock} & {-1, 7}:
                    current_rock_loc = new_rock
                transformations_idx += 1
            else:
                new_rock = {
                    coord - 1j for coord in current_rock_loc}
                if not new_rock & chamber and not {r.imag for r in new_rock} & {-1}:
                    current_rock_loc = new_rock
                else:
                    chamber |= current_rock_loc
                    break
            it_num += 1
        # print(chamber)
        highest_rock = int(max([c.imag for c in chamber]))
        i += 1


print(part_one(get_input()))
print(part_two(get_input()))
