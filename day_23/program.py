from collections import Counter
from collections import defaultdict


def get_input():
    with open("day_23/input.txt") as f:
        file = f.read().splitlines()

    elves = defaultdict(dict)
    for row, line in enumerate(file):
        for col, char in enumerate(line):
            if char == "#":
                elves[col + row*1j] = {"proposed_location": None}

    return elves


def get_adjacent_elves(elves, elf):
    """
    Returned in this order: N, S, E, W, NE, NW, SE, SW
    """
    return [
        elf - 1j,
        elf + 1j,
        elf + 1,
        elf - 1,
        elf + 1 - 1j,
        elf - 1 - 1j,
        elf + 1 + 1j,
        elf - 1 + 1j,
    ]


def part_one(elves):
    direction_list = [-1j, 1j, -1, 1]
    for round in range(10):
        north_idx = direction_list.index(-1j)
        south_idx = direction_list.index(1j)
        east_idx = direction_list.index(1)
        west_idx = direction_list.index(-1)
        for elf in list(elves):
            directions = []
            if not elves[elf]:
                continue
            neighbors = get_adjacent_elves(elves, elf)

            if all(not elves[neighbor] for neighbor in [neighbors[0], neighbors[4], neighbors[5]]):
                directions.append(-1j)
            if all(not elves[neighbor] for neighbor in [neighbors[1], neighbors[6], neighbors[7]]):
                directions.append(1j)
            if all(not elves[neighbor] for neighbor in [neighbors[3], neighbors[5], neighbors[7]]):
                directions.append(-1)
            if all(not elves[neighbor] for neighbor in [neighbors[2], neighbors[4], neighbors[6]]):
                directions.append(1)
            if all(not elves[neighbor] for neighbor in neighbors):
                directions = []
                continue

            min_direction = 1000
            for direction in directions:
                if direction == -1j:
                    min_direction = min(min_direction, north_idx)
                elif direction == 1j:
                    min_direction = min(min_direction, south_idx)
                elif direction == 1:
                    min_direction = min(min_direction, east_idx)
                elif direction == -1:
                    min_direction = min(min_direction, west_idx)
            if min_direction == north_idx:
                elves[elf]["proposed_location"] = elf - 1j
            elif min_direction == south_idx:
                elves[elf]["proposed_location"] = elf + 1j
            elif min_direction == east_idx:
                elves[elf]["proposed_location"] = elf + 1
            elif min_direction == west_idx:
                elves[elf]["proposed_location"] = elf - 1

        locs = [elves[elf]["proposed_location"] for elf in elves if elves[elf]]
        l_c = Counter(locs)
        l_c_1 = {k: c for k, c in l_c.items() if c > 1}
        for elf in elves:
            if elves[elf] and elves[elf]["proposed_location"] in l_c_1:
                elves[elf]["proposed_location"] = None

        for elf in list(elves):
            if elves[elf] and elves[elf]["proposed_location"]:
                elves[elves[elf]["proposed_location"]] = {
                    "proposed_location": None}
                elves[elf] = {}
        direction_list.append(direction_list.pop(0))

    x_min = int(min([elf for elf in list(elves) if elves[elf]],
                key=lambda x: x.real).real)
    x_max = int(max([elf for elf in list(elves) if elves[elf]],
                key=lambda x: x.real).real)

    y_min = int(min([elf for elf in list(elves) if elves[elf]],
                key=lambda x: x.imag).imag)
    y_max = int(max([elf for elf in list(elves) if elves[elf]],
                key=lambda x: x.imag).imag)

    return (x_max-x_min+1)*(y_max-y_min+1) - sum(1 for key, val in elves.items() if val)


def part_two(elves):
    direction_list = [-1j, 1j, -1, 1]
    elf_moved = True
    count = 1
    while elf_moved:
        north_idx = direction_list.index(-1j)
        south_idx = direction_list.index(1j)
        east_idx = direction_list.index(1)
        west_idx = direction_list.index(-1)
        for elf in list(elves):
            directions = []
            if not elves[elf]:
                continue
            neighbors = get_adjacent_elves(elves, elf)

            if all(not elves[neighbor] for neighbor in [neighbors[0], neighbors[4], neighbors[5]]):
                directions.append(-1j)
            if all(not elves[neighbor] for neighbor in [neighbors[1], neighbors[6], neighbors[7]]):
                directions.append(1j)
            if all(not elves[neighbor] for neighbor in [neighbors[3], neighbors[5], neighbors[7]]):
                directions.append(-1)
            if all(not elves[neighbor] for neighbor in [neighbors[2], neighbors[4], neighbors[6]]):
                directions.append(1)
            if all(not elves[neighbor] for neighbor in neighbors):
                directions = []
                continue

            min_direction = 1000
            for direction in directions:
                if direction == -1j:
                    min_direction = min(min_direction, north_idx)
                elif direction == 1j:
                    min_direction = min(min_direction, south_idx)
                elif direction == 1:
                    min_direction = min(min_direction, east_idx)
                elif direction == -1:
                    min_direction = min(min_direction, west_idx)
            if min_direction == north_idx:
                elves[elf]["proposed_location"] = elf - 1j
            elif min_direction == south_idx:
                elves[elf]["proposed_location"] = elf + 1j
            elif min_direction == east_idx:
                elves[elf]["proposed_location"] = elf + 1
            elif min_direction == west_idx:
                elves[elf]["proposed_location"] = elf - 1

        locs = [elves[elf]["proposed_location"] for elf in elves if elves[elf]]
        l_c = Counter(locs)

        l_c_1 = {k: c for k, c in l_c.items() if c != 1 and k != 0j}
        if all(c != 1 for k, c in l_c.items()):
            break

        for elf in elves:
            if elves[elf] and elves[elf]["proposed_location"] in l_c_1:
                if elves[elf]["proposed_location"] == 0j:
                    print(elf)
                elves[elf]["proposed_location"] = None
        elf_moved = False
        for elf in list(elves):
            if elves[elf] and elves[elf]["proposed_location"] != None:
                elves[elves[elf]["proposed_location"]] = {
                    "proposed_location": None}
                elves[elf] = {}
        elf_moved = True
        direction_list.append(direction_list.pop(0))
        count += 1
        x_min = int(min([elf for elf in list(elves) if elves[elf]],
                        key=lambda x: x.real).real)
        x_max = int(max([elf for elf in list(elves) if elves[elf]],
                    key=lambda x: x.real).real)

        y_min = int(min([elf for elf in list(elves) if elves[elf]],
                    key=lambda x: x.imag).imag)
        y_max = int(max([elf for elf in list(elves) if elves[elf]],
                        key=lambda x: x.imag).imag)
        if count in (509, 510, 511, 512):
            s = ""
            for row in range(y_min, y_max+1):
                for col in range(x_min, x_max+1):
                    if col + row*1j == 1 + 0j and elves[1+0j]:
                        s += "X"
                    elif elves[col + row*1j]:
                        s += "#"
                    else:
                        s += ","
                s += "\n"
            with open(f"{count}.txt", "w") as f:
                f.write(s)

    return count


print(part_one(get_input()))
print(part_two(get_input()))
