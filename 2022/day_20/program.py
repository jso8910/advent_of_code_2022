from itertools import cycle
from collections import deque


def get_input():
    with open("day_20/input.txt", "r") as f:
        file = f.read().splitlines()

    return [{"id": idx, "num": int(num)} for idx, num in enumerate(file)]


def part_one(data):
    mixed = deque(data)
    l_data = len(data)
    for thing in data:
        idx = mixed.index(thing)
        # Rotate item to the end of the deque
        mixed.rotate(l_data - idx - 1)
        num = mixed.pop()
        # Rotate new position of item to end of deque
        mixed.rotate(l_data - num["num"] - 1)
        mixed.append(num)

    data = list(mixed)
    idx_0 = [idx for idx in range(len(data)) if data[idx]["num"] == 0][0]
    d = cycle(data[idx_0:] + data[:idx_0])
    s = 0
    for idx, l in enumerate(d):
        if (idx + 0) % 1000 == 0 and idx != 0:
            s += l["num"]
            if idx + 0 == 3000:
                break
    return s


def part_two(data):
    data = [{"num": x["num"]*811589153, "id": x["id"]} for x in data]
    mixed = deque(data)
    l_data = len(data)
    for i in range(10):
        for thing in data:
            idx = mixed.index(thing)
            # Rotate item to the end of the deque
            mixed.rotate(l_data - idx - 1)
            num = mixed.pop()
            # Rotate new position of item to end of deque
            mixed.rotate(l_data - num["num"] - 1)
            mixed.append(num)

    data = list(mixed)
    idx_0 = [idx for idx in range(len(data)) if data[idx]["num"] == 0][0]
    d = cycle(data[idx_0:] + data[:idx_0])
    s = 0
    for idx, l in enumerate(d):
        if (idx + 0) % 1000 == 0 and idx != 0:
            s += l["num"]
            if idx + 0 == 3000:
                break
    return s


print(part_one(get_input()))
print(part_two(get_input()))
