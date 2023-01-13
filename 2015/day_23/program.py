def get_input():
    with open("day_23/input.txt", "r") as f:
        file = f.read().splitlines()

    instructions = []
    for line in file:
        instructions.append(line.replace(",", "").split(" "))

    for instruction in instructions:
        for idx, thing in enumerate(instruction):
            if thing[1:].isnumeric():
                instruction[idx] = int(thing)

    return instructions


def part_one(instructions):
    a = 0
    b = 0
    i = 0
    while i < len(instructions):
        instruction = instructions[i]
        match instruction[0]:
            case "hlf":
                if instruction[1] == "a":
                    a /= 2
                else:
                    b /= 2
            case "tpl":
                if instruction[1] == "a":
                    a *= 3
                else:
                    b *= 3
            case "inc":
                if instruction[1] == "a":
                    a += 1
                else:
                    b += 1
            case "jmp":
                i += instruction[1]
                continue
            case "jie":
                if instruction[1] == "a":
                    if a % 2 == 0:
                        i += instruction[2]
                        continue
                else:
                    if b % 2 == 0:
                        i += instruction[2]
                        continue
            case "jio":
                if instruction[1] == "a":
                    if a == 1:
                        i += instruction[2]
                        continue
                else:
                    if b == 1:
                        i += instruction[2]
                        continue
        i += 1

    return b


def part_one(instructions):
    a = 1
    b = 0
    i = 0
    while i < len(instructions):
        instruction = instructions[i]
        match instruction[0]:
            case "hlf":
                if instruction[1] == "a":
                    a /= 2
                else:
                    b /= 2
            case "tpl":
                if instruction[1] == "a":
                    a *= 3
                else:
                    b *= 3
            case "inc":
                if instruction[1] == "a":
                    a += 1
                else:
                    b += 1
            case "jmp":
                i += instruction[1]
                continue
            case "jie":
                if instruction[1] == "a":
                    if a % 2 == 0:
                        i += instruction[2]
                        continue
                else:
                    if b % 2 == 0:
                        i += instruction[2]
                        continue
            case "jio":
                if instruction[1] == "a":
                    if a == 1:
                        i += instruction[2]
                        continue
                else:
                    if b == 1:
                        i += instruction[2]
                        continue
        i += 1

    return b


print(part_one(get_input()))
