from math import gcd


def get_input():
    with open("day_20/input.txt", "r") as f:
        return int(f.read())


def factorize(n):
    for a in range(1, int(n**0.5)+1):
        if n % a:
            continue
        yield from {a, n//a}


def part_one(target_num):
    # Also equal to the maximum house
    actual_num = target_num // 10
    for house in range(1, actual_num + 1):
        if sum(factorize(house)) >= actual_num:
            return house


def part_two(target_num):
    # Also equal to the maximum house
    actual_num = target_num / 11
    for house in range(1, int(actual_num) + 1):
        if sum(factor for factor in factorize(house) if house / factor <= 50) >= actual_num:
            return house


print(part_one(get_input()))
print(part_two(get_input()))
