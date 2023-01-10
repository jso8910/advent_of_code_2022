def get_input():
    with open("day_1/input.txt", "r") as f:
        file = f.read()

    nums = [1 if c == "(" else -1 for c in file]
    return nums


def part_one(nums):
    return sum(nums)


def part_two(nums):
    return [part_one(nums[:i]) for i in range(len(nums))].index(-1)


print(part_one(get_input()))
print(part_two(get_input()))
