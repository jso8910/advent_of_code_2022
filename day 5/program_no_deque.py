import itertools


def rotate_matrix(A):
    new = list(map(list, itertools.zip_longest(*A, fillvalue=None)))
    for idx, n in enumerate(new):
        new[idx] = list(thing for thing in n if thing != ' ')
    return new


def move_pile(start: list[str], end: list[str]):
    end.append(start.pop())
    return start, end


def move_pile_part_two(start: list[str], end: list[str], number_moved: int):
    for i in range(number_moved, 0, -1):
        end.append(start[len(start) - i - 1])
        del start[len(start) - i - 1]
    return start, end


def get_input():
    with open("day 5/input.txt", "r") as f:
        input_initial, file = f.read().split('\n\n')
    input_initial = input_initial.splitlines()[:-1]
    stacks = []
    for line in input_initial:
        stacks.append([])
        for i in range(9):
            stacks[-1].append(line[1 + 4*i])

    stacks = rotate_matrix(stacks)
    for index in range(len(stacks)):
        stacks[index].reverse()
    return stacks, file.splitlines()


def part_one(stacks, file):
    for line in file:
        line = line.strip()
        number_moved = int(line.split("move ")[1].split(" ")[0])
        start = int(line.split("from ")[1].split(" ")[0]) - 1
        end = int(line.split("to ")[1].split(" ")[0]) - 1
        for i in range(number_moved):
            move_pile(
                stacks[start], stacks[end])

    print(''.join([thing[-1] for thing in stacks]))


def part_two(stacks, file):
    for line in file:
        line = line.strip()
        number_moved = int(line.split("move ")[1].split(" ")[0])
        start = int(line.split("from ")[1].split(" ")[0]) - 1
        end = int(line.split("to ")[1].split(" ")[0]) - 1
        move_pile_part_two(
            stacks[start], stacks[end], number_moved)

    print(''.join([thing[-1] for thing in stacks]))


part_one(*get_input())
part_two(*get_input())
