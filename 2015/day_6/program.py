from collections import defaultdict


def get_input():
    with open("day_6/input.txt", "r") as f:
        file = f.read().splitlines()

    instructions = []
    for instruction in file:
        instructions.append({})
        words = instruction.replace(",", " ").split(" ")
        match words:
            case ["toggle", x1, y1, "through", x2, y2]:
                instructions[-1]["instruction"] = "toggle"
                instructions[-1]["c1"] = int(x1) + int(y1)*1j
                instructions[-1]["c2"] = int(x2) + int(y2)*1j
            case ["turn", "off", x1, y1, "through", x2, y2]:
                instructions[-1]["instruction"] = "off"
                instructions[-1]["c1"] = int(x1) + int(y1)*1j
                instructions[-1]["c2"] = int(x2) + int(y2)*1j
            case ["turn", "on", x1, y1, "through", x2, y2]:
                instructions[-1]["instruction"] = "on"
                instructions[-1]["c1"] = int(x1) + int(y1)*1j
                instructions[-1]["c2"] = int(x2) + int(y2)*1j

    return instructions


def part_one(instructions):
    grid = defaultdict(bool)
    def toggle(x, y): return 1 - grid[x+y*1j]
    def on(x, y): return 1
    def off(x, y): return 0
    for instruction in instructions:
        match instruction["instruction"]:
            case "toggle":
                func = toggle
            case "on":
                func = on
            case "off":
                func = off
            case _:
                print(instruction)
        xes = sorted((int(instruction["c1"].real), int(
            instruction["c2"].real)))
        ys = sorted((int(instruction["c1"].imag), int(
            instruction["c2"].imag)))
        for x in range(xes[0], xes[1] + 1):
            for y in range(ys[0], ys[1] + 1):
                grid[x+y*1j] = func(x, y)

    return sum(grid.values())


def part_two(instructions):
    grid = defaultdict(bool)
    def toggle(x, y, i): return i+2
    def on(x, y, i): return i+1
    def off(x, y, i): return i-1 if i else 0
    for instruction in instructions:
        match instruction["instruction"]:
            case "toggle":
                func = toggle
            case "on":
                func = on
            case "off":
                func = off
            case _:
                print(instruction)
        xes = sorted((int(instruction["c1"].real), int(
            instruction["c2"].real)))
        ys = sorted((int(instruction["c1"].imag), int(
            instruction["c2"].imag)))
        for x in range(xes[0], xes[1] + 1):
            for y in range(ys[0], ys[1] + 1):
                grid[x+y*1j] = func(x, y, grid[x+y*1j])

    return sum(grid.values())


print(part_one(get_input()))
print(part_two(get_input()))
