def get_input():
    with open("day_21/input.txt", "r") as f:
        file = f.read().splitlines()

    numbers = {}
    for n in file:
        if len(n.split(" ")) == 2:
            numbers[n.split(":")[0]] = int(n.split(" ")[1])
        else:
            numbers[n.split(":")[0]] = [n.split(" ")[1],
                                        n.split(" ")[2], n.split(" ")[3]]

    for key, n in numbers.items():
        if isinstance(n, list):
            numbers[key][0] = numbers[n[0]]
            numbers[key][2] = numbers[n[2]]

    # NOTE I looked at the numbers["root"] for the example input and i get 155 instead of 152. What's my issue?

    return numbers


def walk_tree(numbers, humn=None, humn_val=None):
    num_1 = numbers[0]
    op = numbers[1]
    num_2 = numbers[2]
    if isinstance(num_1, list):
        num_1 = walk_tree(num_1, humn=humn, humn_val=humn_val)
    if num_1 == humn:
        num_1 = humn_val
    if isinstance(num_2, list):
        num_2 = walk_tree(num_2, humn=humn, humn_val=humn_val)
    if num_2 == humn:
        num_2 = humn_val

    res = num_1
    match op:
        case "+":
            res += num_2
        case "-":
            res -= num_2
        case "*":
            res *= num_2
        case "/":
            res /= num_2
    return res


def in_tree(numbers, val):
    if val in (numbers[0], numbers[2]):
        return True

    v_1 = False
    v_2 = False

    if isinstance(numbers[0], list):
        v_1 = in_tree(numbers[0], val)
    if isinstance(numbers[2], list):
        v_2 = in_tree(numbers[2], val)

    return v_1 or v_2


def part_one(numbers):
    root = numbers["root"]
    return int(walk_tree(root))


def part_two(numbers):
    n_1 = numbers["root"][0]
    n_2 = numbers["root"][2]
    humn = numbers["humn"]
    num_1_val = walk_tree(n_1)
    num_2_val = walk_tree(n_2)
    thousand_vals = []
    if in_tree(n_1, humn):
        i = 0
        j = 0
        while True:
            if walk_tree(n_1, humn=humn, humn_val=i) == num_2_val:
                return i
            if i % 1000 == 0:
                thousand_vals.append(
                    int(walk_tree(n_1, humn=humn, humn_val=i)))
                if len(thousand_vals) >= 3:
                    rate_of_change = (
                        thousand_vals[-1] - thousand_vals[0]) / (len(thousand_vals) * 1000)
                    remaining = (
                        num_2_val - thousand_vals[-1]) / rate_of_change
                    i += (remaining)
                    i = round(i)
                    thousand_vals = []
                # print(i)
                # print(j, i, int(walk_tree(n_1, humn=humn, humn_val=i)), num_2_val)
            i += 1
            j += 1
    elif in_tree(n_2, humn):
        i = 0
        while True:
            if int(walk_tree(n_2, humn=humn, humn_val=i)) == int(num_1_val):
                return i
            i += 1
            if i % 1000 == 0:
                thousand_vals.append(
                    int(walk_tree(n_1, humn=humn, humn_val=i)))
                if len(thousand_vals) >= 3:
                    rate_of_change = (
                        thousand_vals[-1] - thousand_vals[0]) / (len(thousand_vals) * 1000)
                    remaining = (
                        num_2_val - thousand_vals[-1]) / rate_of_change
                    i += (remaining)
                    i = round(i)
                    thousand_vals = []


# pprint(get_input()["root"])
print(part_one(get_input()))
print(part_two(get_input()))
