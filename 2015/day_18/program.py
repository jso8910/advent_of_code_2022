from collections import defaultdict


def get_input():
    with open("day_18/input.txt", "r") as f:
        file = f.read().splitlines()

    lights = defaultdict(bool)
    for y, line in enumerate(file):
        for x, char in enumerate(line):
            lights[x + y*1j] = char == "#"

    for x in range(len(file[0])):
        lights[x - 1j] = False
        lights[x + len(file)*1j] = False

    for y in range(len(file)):
        lights[-1 + y*1j] = False
        lights[len(file[0]) + y*1j] = False

    return lights, len(file[0]), len(file)


def part_one(lights, cols, rows):
    for i in range(100):
        new_lights = defaultdict(bool)
        for light in list(lights.keys()):
            if cols <= light.real or light.real < 0 or rows <= light.imag or light.imag < 0:
                continue
            neighbors = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x == y == 0:
                        continue
                    if lights[light + x + y*1j]:
                        neighbors += 1

            if lights[light]:
                new_lights[light] = neighbors == 2 or neighbors == 3
            else:
                new_lights[light] = neighbors == 3
        lights = new_lights

    return list(lights.values()).count(True)


def part_two(lights, cols, rows):
    lights[0] = True
    lights[(rows - 1) * 1j] = True
    lights[cols - 1] = True
    lights[cols - 1 + (rows - 1) * 1j] = True
    for i in range(100):
        new_lights = defaultdict(bool)
        for light in list(lights.keys()):
            if cols <= light.real or light.real < 0 or rows <= light.imag or light.imag < 0:
                continue
            if light in [0, (rows - 1) * 1j, cols - 1, cols - 1 + (rows - 1) * 1j]:
                new_lights[light] = True
                continue
            neighbors = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x == y == 0:
                        continue
                    if lights[light + x + y*1j]:
                        neighbors += 1

            if lights[light]:
                new_lights[light] = neighbors == 2 or neighbors == 3
            else:
                new_lights[light] = neighbors == 3
        lights = new_lights

    return list(lights.values()).count(True)


print(part_one(*get_input()))
print(part_two(*get_input()))
