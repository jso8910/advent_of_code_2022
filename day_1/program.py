def part_one():
    with open("day_1/input.txt", "r") as f:
        file = f.read()

    elves = file.split("\n\n")
    elves = [[int(calories) for calories in elf.split("\n")] for elf in elves]
    elves_by_calories = sorted([sum(elf) for elf in elves], reverse=True)

    return elves_by_calories[0]


def part_two():
    with open("day_1/input.txt", "r") as f:
        file = f.read()

    elves = file.split("\n\n")
    elves = [[int(calories) for calories in elf.split("\n")] for elf in elves]
    elves_by_calories = sorted([sum(elf) for elf in elves], reverse=True)

    return sum(elves_by_calories[0:3])


print(part_one())
print(part_two())
