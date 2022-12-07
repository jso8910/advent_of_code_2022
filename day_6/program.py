def get_input():
    with open("day_6/input.txt", "r") as f:
        return f.read()


def part_one(file):
    LEN_MARKER = 4
    marker_end = 0
    for i in range(len(file)):
        if len(set(file[i:i+LEN_MARKER])) == LEN_MARKER:
            marker_end = i + LEN_MARKER
            break
    return marker_end


def part_two(file):
    LEN_MARKER = 14
    marker_end = 0
    for i in range(len(file)):
        if len(set(file[i:i+LEN_MARKER])) == LEN_MARKER:
            marker_end = i + LEN_MARKER
            break
    return marker_end


print(part_one(get_input()))
print(part_two(get_input()))
