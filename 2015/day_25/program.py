import re
from collections import defaultdict


def get_input():
    with open("day_25/input.txt", "r") as f:
        file = f.read()

    prog = re.compile(
        r"To continue, please consult the code grid in the manual.  Enter the code at row (\d+), column (\d+).")
    row, col = prog.match(file).groups()
    return int(row), int(col)


def part_one(row, col):
    grid = defaultdict(lambda: None)
    grid[1 + 1j] = 20151125
    current_coord = 1 + 1j
    while not grid[col + row * 1j]:
        prev_value = grid[current_coord]
        if (current_coord - 1j).imag <= 0:
            current_coord = (current_coord.real + 1)*1j + 1
        else:
            current_coord += 1-1j

        # A * B MOD C = ((A MOD C) * (B MOD C)) MOD C
        new_value = ((prev_value % 33554393) * (252533 % 33554393)) % 33554393
        grid[current_coord] = new_value
        # print(current_coord)

    return grid[col + row * 1j]


print(part_one(*get_input()))
