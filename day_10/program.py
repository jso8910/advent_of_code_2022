def load_input():
    with open("day_10/input.txt", "r") as f:
        file = f.read().splitlines()

    # Contains the number added to the X register during that cycle
    cycles = []
    for line in file:
        match line.split(" "):
            case ["noop"]:
                cycles.append(0)
            case ["addx", n]:
                cycles.extend([0, int(n)])   # Takes 2 clock cycles

    return cycles


def part_one(cycles):
    STARTING_VAL = 1
    MAX = 220
    MIN = 20
    INTERVAL = 40

    # Pretty simple, sum of [0, i-1) because, for the example of the value at cycle 20 (index 19), cycle 20 hasn't finished executing yet
    total = sum([(sum(cycles[:i-1]) + STARTING_VAL)
                * i for i in range(MIN, MAX + 1, INTERVAL)])

    return total


def part_two(cycles):
    STARTING_VAL = 1
    MAX = 239
    MIN = 0
    # Pretty simple, sum of [0, i)
    x_per_cycle = [(sum(cycles[:i]) + STARTING_VAL)
                   for i in range(MIN, MAX + 1)]

    scan = 0b1
    for i in range(MIN, MAX):
        scan = scan << 1
        if (i) % 40 == 0:
            scan = 0b1
            print()
        mask = (2**(x_per_cycle[i]) if x_per_cycle[i] >= 0 else 0) + \
            (2**(x_per_cycle[i]-1) if x_per_cycle[i] -
             1 >= 0 else 0) + (2**(x_per_cycle[i]+1) if x_per_cycle[i] + 1 >= 0 else 0)
        if mask & scan:
            print("#", end="")
        else:
            print(" ", end="")
    print()


print(part_one(load_input()))
part_two(load_input())
