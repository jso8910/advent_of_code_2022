import string


def part_one():
    with open("day 3/input.txt", "r") as f:
        file = f.readlines()
    priorities = {letter: priority + 1 for priority,
                  letter in enumerate(string.ascii_letters)}

    priority_sum = 0
    for rucksack in file:
        items = {}  # format: dict[str, bool]
        first_compartment = rucksack[len(rucksack)//2:]
        second_compartment = rucksack[:len(rucksack)//2]
        for item in first_compartment:
            items[item] = True
        for item in second_compartment:
            if item in items:
                priority_sum += priorities[item]
                break

    print(priority_sum)


def part_two():
    with open("day 3/input.txt", "r") as f:
        file = f.readlines()
    priorities = {letter: priority + 1 for priority,
                  letter in enumerate(string.ascii_letters)}

    groups: list[list[str]] = []
    for i in range(0, len(file), 3):
        groups.append(file[i:i + 3])

    priority_sum = 0
    for group in groups:
        items = {}  # format: dict[str, list[bool]]
        for rucksack in group:
            rucksack = rucksack.strip()
            ruck_items = []
            for item in rucksack:
                if item in items and not item in ruck_items:
                    ruck_items.append(item)
                    items[item].append(True)
                elif not item in ruck_items:
                    ruck_items.append(item)
                    items[item] = [True]
        for key, value in items.items():
            if value == [True, True, True]:
                priority_sum += priorities[key]

    print(priority_sum)


part_two()
