from hashlib import md5


def get_input():
    with open("day_4/input.txt", "r") as f:
        return f.read()


def part_one(key):
    i = 0
    hash = md5("".encode('utf-8')).hexdigest()
    while hash[:5] != "00000":
        i += 1
        hash = md5((key + str(i)).encode('utf-8')).hexdigest()
    return i


def part_two(key):
    i = 0
    hash = md5("".encode('utf-8')).hexdigest()
    while hash[:6] != "000000":
        i += 1
        hash = md5((key + str(i)).encode('utf-8')).hexdigest()
    return i


print(part_one(get_input()))
print(part_two(get_input()))
