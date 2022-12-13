from copy import deepcopy
from ast import literal_eval


def get_input():
    with open("day_13/input.txt") as f:
        file = f.read().split("\n\n")

    pairs = []
    for pair in file:
        pairs.append(
            (literal_eval(pair.splitlines()[0]), literal_eval(pair.splitlines()[1])))

    return pairs


def get_input_p2():
    with open("day_13/input.txt") as f:
        file = f.read().replace("\n\n", "\n").splitlines()

    elements = []
    for element in file:
        elements.append(eval(element))

    return elements


def switch_pair(pair):
    if isinstance(pair[0], int) and isinstance(pair[1], int):
        if pair[0] < pair[1]:
            return False
        elif pair[0] > pair[1]:
            return True
        else:
            return None

    if isinstance(pair[0], int) and isinstance(pair[1], list):
        return switch_pair(([pair[0]], pair[1]))

    if isinstance(pair[0], list) and isinstance(pair[1], int):
        return switch_pair((pair[0], [pair[1]]))

    if isinstance(pair[0], list) and isinstance(pair[1], list):
        if len(pair[0]) > 0 and len(pair[1]) > 0:
            check_el = switch_pair((pair[0][0], pair[1][0]))
            if check_el:
                return True
            elif check_el == False:
                return False
            else:
                if len(pair[0]) > 1 and len(pair[1]) > 1:
                    return switch_pair((pair[0][1:], pair[1][1:]))
                elif len(pair[0]) > len(pair[1]):
                    return True
                elif len(pair[0]) < len(pair[1]):
                    return False
                else:
                    return None
        elif len(pair[0]) > len(pair[1]):
            return True
        elif len(pair[0]) < len(pair[1]):
            return False
        else:
            return None


def part_one(pairs):
    pairs_correct = 0
    for idx, pair in enumerate(pairs):
        if not switch_pair(pair):
            pairs_correct += idx + 1

    return pairs_correct


# Wow this is inefficient but it works :P
def part_two(elements):
    elements.append([[2]])
    elements.append([[6]])
    for i in range(len(elements) - 1):
        for j in range(len(elements) - i - 1):
            if switch_pair((elements[j], elements[j+1])):
                temp = deepcopy(elements[j])
                elements[j] = deepcopy(elements[j+1])
                elements[j+1] = temp

    return (elements.index([[2]]) + 1) * (elements.index([[6]]) + 1)


print(part_one(get_input()))
print(part_two(get_input_p2()))
