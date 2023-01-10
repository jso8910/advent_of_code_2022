def get_input():
    with open("day_10/input.txt", "r") as f:
        return f.read()


def look_and_say(num: str):
    new_str = ""
    temp = ""
    for char in num:
        if not temp or char == temp[0]:
            temp += char
        else:
            new_str += str(len(temp)) + temp[0]
            temp = char
    new_str += str(len(temp)) + temp[0]
    return new_str


def part_one(num):
    for i in range(40):
        num = look_and_say(num)

    return len(num)


def part_two(num):
    for i in range(50):
        num = look_and_say(num)

    return len(num)


print(part_one(get_input()))
print(part_two(get_input()))
