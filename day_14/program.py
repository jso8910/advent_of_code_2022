from collections import defaultdict


def get_input():
    with open("day_14/input.txt", 'r') as f:
        file = f.read().splitlines()

    shapes: list[complex] = []
    for shape in file:
        shapes.append([int(vertex.split(",")[0]) + int(vertex.split(",")[1])*1j
                      for vertex in shape.split("->")])

    # False means nothing, True means blocked (doesn't matter if it's sand)
    grid = defaultdict(bool)
    for shape in shapes:
        for vertex_pair in zip(shape, shape[1:]):
            if vertex_pair[0].real == vertex_pair[1].real:
                sorted_by_imag = list(map(int, sorted(
                    [vertex_pair[0].imag, vertex_pair[1].imag])))
                for i in range(sorted_by_imag[0], sorted_by_imag[1]+1):
                    grid[vertex_pair[0].real + i*1j] = True
            else:   # If both are different or same, something is wrong
                sorted_by_real = list(map(int, sorted(
                    [vertex_pair[0].real, vertex_pair[1].real])))
                for i in range(sorted_by_real[0], sorted_by_real[1]+1):
                    grid[i + vertex_pair[0].imag*1j] = True

    return grid


def move_down(grid, sand, floor=None):
    if floor:
        if (sand + 1j).imag > floor - 1:    # lowest valid pos is above the floor
            return sand
    if not grid[sand + 1j]:
        return sand + 1j
    elif grid[sand + 1j] and not grid[sand + 1j - 1]:   # Go to the left by default
        return sand + 1j - 1
    elif grid[sand + 1j] and not grid[sand + 1j + 1]:
        return sand + 1j + 1
    else:
        # It hasn't moved at all, this will be handled
        return sand


def part_one(grid: dict[complex, bool]):
    generator = 500 + 0j
    # Default loc
    current_sand = generator

    count_sand = 0

    sand_falling_inf = False

    highest_y = 0
    for key in grid:
        if key.imag > highest_y:
            highest_y = key.imag

    while not sand_falling_inf:
        new_sand = move_down(grid, current_sand)
        if new_sand == current_sand:
            count_sand += 1
            grid[new_sand] = True
            current_sand = generator
        else:
            current_sand = new_sand

        sand_falling_inf = True
        for y in range(int(current_sand.imag), int(highest_y) + 1):
            # Check if there's anything to fall on
            if grid[current_sand.real + y*1j]:
                sand_falling_inf = False
                break

    return count_sand


def part_two(grid):
    generator = 500 + 0j
    highest_y = 0
    for key in grid:
        if key.imag > highest_y:
            highest_y = key.imag

    floor = highest_y + 2

    count_sand = 0

    # Default loc
    current_sand = generator

    while True:
        new_sand = move_down(grid, current_sand, floor=floor)
        if new_sand == current_sand:
            count_sand += 1
            grid[new_sand] = True
            if new_sand == generator:
                break
            current_sand = generator
        else:
            current_sand = new_sand

    return count_sand


print(part_one(get_input()))
print(part_two(get_input()))
