import math


def column(list, i):
    return [row[i] for row in list]


def load_input():
    with open("day_8/input.txt", "r") as f:
        file = f.read().splitlines()

    trees = []
    for line in file:
        trees.append(list(map(int, list(line))))

    return trees


def number_of_trees(list):
    for idx, it in enumerate(list):
        if it:
            return idx + 1

    return len(list)


def part_one(trees):
    exposed = 0
    for idx_row, row_trees in enumerate(trees):
        for idx_col, tree in enumerate(row_trees):
            col_trees = column(trees, idx_col)

            # Add [-1] just in case it's an edge
            trees_around = [
                max(row_trees[:idx_col] + [-1]),        # Trees to the left
                max(row_trees[idx_col + 1:] + [-1]),    # Trees to the right
                max(col_trees[:idx_row] + [-1]),        # Trees above
                max(col_trees[idx_row + 1:] + [-1]),    # Trees below
            ]

            # If any of these values are less than the tree, it is exposed
            if tree > min(trees_around):
                exposed += 1

    return exposed


def part_two(trees):
    max_scenic = 0
    for idx_row, row_trees in enumerate(trees):
        for idx_col, tree in enumerate(row_trees):
            col_trees = column(trees, idx_col)

            # Add [-1] just in case it's an edge
            scenic_score = math.prod([
                number_of_trees(list(map(lambda x: x >= tree,
                                         (row_trees[:idx_col])[::-1]))),   # Trees to the left. Reverses the list so the current tree is before index 0
                number_of_trees(list(map(lambda x: x >= tree,
                                         row_trees[idx_col + 1:]))),       # Trees to the right. Reverses the list so the current tree is before index 0
                number_of_trees(list(map(lambda x: x >= tree,
                                         col_trees[:idx_row]))[::-1]),     # Trees above
                number_of_trees(list(map(lambda x: x >= tree,
                                         col_trees[idx_row + 1:]))),       # Trees below
            ])
            if scenic_score > max_scenic:
                max_scenic = scenic_score

    return max_scenic


print(part_one(load_input()))
print(part_two(load_input()))
