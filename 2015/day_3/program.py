STEPS = {
    "^": -1j,
    ">": 1,
    "v": 1j,
    "<": -1
}


def get_input():
    with open("day_3/input.txt", "r") as f:
        file = f.read()

    steps = []
    for char in file:
        steps.append(STEPS[char])

    return steps


def part_one(steps):
    visited = {}
    current = 0
    visited[current] = True
    for step in steps:
        current += step
        visited[current] = True

    return sum(visited.values())


def part_two(steps):
    steps_1 = steps[::2]
    steps_2 = steps[1::2]
    visited = {}
    current = 0
    visited[current] = True
    for step in steps_1:
        current += step
        visited[current] = True

    current = 0
    for step in steps_2:
        current += step
        visited[current] = True

    return sum(visited.values())


print(part_one(get_input()))
print(part_two(get_input()))
