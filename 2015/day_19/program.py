from itertools import combinations
from collections import defaultdict


def get_input():
    with open("day_19/input.txt", "r") as f:
        file = f.read().splitlines()
    molecule_transforms = []
    for line in file:
        if "=>" in line:
            molecule_transforms.append(
                line.split(" => "))
    return molecule_transforms, file[-1]


def gen_transforms(medicine, molecule_transforms):
    temp = ""
    transformations = {}
    transform_keys = [thing[0] for thing in molecule_transforms]
    for idx, char in enumerate(medicine):
        if char not in transform_keys and not temp:
            temp += char
        elif temp + char not in transform_keys:
            temp = char
        else:
            transformations[(idx-len(temp), idx)
                            ] = [thing[1] for thing in molecule_transforms if thing[0] == (temp + char)]
            temp = ""
    return transformations


def part_one(molecule_transforms, medicine):
    temp = ""
    transformations = gen_transforms(medicine, molecule_transforms)

    medicine_transformed = set()
    for transformation in transformations:
        for res in transformations[transformation]:
            new_medicine = medicine[:transformation[0]
                                    ] + res + medicine[transformation[1]:]
            medicine_transformed.add(new_medicine)

    return len(medicine_transformed)


def bfs(molecule_transforms, start, end="e"):
    visited = set()
    original_transforms = molecule_transforms.copy()
    node = start
    depth = 0
    while node != end:
        try:
            f = max(molecule_transforms, key=lambda x: len(x[1]))
        except ValueError:
            molecule_transforms = original_transforms.copy()
            f = max(molecule_transforms, key=lambda x: len(x[1]))
        visited.add(node)
        before, after = f
        new = node.replace(after, before, 1)
        if new != node:
            depth += 1
        else:
            molecule_transforms.remove(f)
        node = new
    return depth


print(part_one(*get_input()))
print(bfs(*get_input()))
