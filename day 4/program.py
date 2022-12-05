def part_one():
    with open("day 4/input.txt", "r") as f:
        file = f.readlines()

    pairs: list[list[list[int]]] = []
    for pair in file:
        pair = pair.strip()
        elf_one = pair.split(",")[0]
        elf_two = pair.split(",")[1]
        pairs.append([range(int(elf_one.split("-")[0]), int(elf_one.split("-")[1]) + 1),
                     range(int(elf_two.split("-")[0]), int(elf_two.split("-")[1]) + 1)])

    count_fully_containing = 0
    for pair in pairs:
        longer_pair = pair[0] if len(pair[0]) > len(pair[1]) else pair[1]
        # print(longer_pair)
        shorter_pair = pair[1] if len(pair[1]) < len(pair[0]) else pair[0]
        x = set(longer_pair)
        if x.intersection(shorter_pair) == set(shorter_pair):
            count_fully_containing += 1
    print(count_fully_containing)


def part_two():
    with open("day 4/input.txt", "r") as f:
        file = f.readlines()

    pairs: list[list[list[int]]] = []
    for pair in file:
        pair = pair.strip()
        elf_one = pair.split(",")[0]
        elf_two = pair.split(",")[1]
        pairs.append([range(int(elf_one.split("-")[0]), int(elf_one.split("-")[1]) + 1),
                     range(int(elf_two.split("-")[0]), int(elf_two.split("-")[1]) + 1)])

    count_intersecting = 0
    for pair in pairs:
        longer_pair = pair[0] if len(pair[0]) > len(pair[1]) else pair[1]
        # print(longer_pair)
        shorter_pair = pair[1] if len(pair[1]) < len(pair[0]) else pair[0]
        x = set(longer_pair)
        if x.intersection(shorter_pair) != set():
            count_intersecting += 1
    print(count_intersecting)


part_two()
