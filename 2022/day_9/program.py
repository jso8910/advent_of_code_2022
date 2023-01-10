def load_input():
    with open("day_9/input.txt", "r") as f:
        file = f.read().splitlines()

    moves = []
    for line in file:
        moves.append(
            {"dir": line.split(' ')[0], "spaces": int(line.split(' ')[1])})

    return moves


VERT_ABS = [1, 0]
HOR_ABS = [0, 1]

UP = [-1, 0]
DOWN = [1, 0]
LEFT = [0, -1]
RIGHT = [0, 1]

MOVES = {
    "U": UP,
    "D": DOWN,
    "L": LEFT,
    "R": RIGHT
}


def follow(knot, tail):
    new_head_diff_from_old = list(
        map(int.__sub__, knot, tail))
    if abs(new_head_diff_from_old[0]) <= 1 and abs(new_head_diff_from_old[1]) <= 1:
        tail = tail
    elif abs(new_head_diff_from_old[1]) == 0:
        tail[0] += 1 if new_head_diff_from_old[0] == 2 else -1
    elif abs(new_head_diff_from_old[0]) == 0:
        tail[1] += 1 if new_head_diff_from_old[1] == 2 else -1
    else:
        tail[0] += 1 if new_head_diff_from_old[0] > 0 else -1
        tail[1] += 1 if new_head_diff_from_old[1] > 0 else -1

    return tail


def part_one(moves):
    grid = [[True]]
    current_head_idx = [0, 0]
    current_tail_idx = [0, 0]
    for move in moves:
        for i in range(move['spaces']):
            move_dir = MOVES[move['dir']]
            current_head_idx[0] += move_dir[0]
            current_head_idx[1] += move_dir[1]
            if current_head_idx[0] < 0:
                grid.insert(0, [False] * len(grid[0]))
                current_head_idx[0] += 1
                current_tail_idx[0] += 1
            elif current_head_idx[0] > len(grid) - 1:
                grid.append([False] * len(grid[0]))
            elif current_head_idx[1] < 0:
                [row.insert(0, False) for row in grid]
                current_head_idx[1] += 1
                current_tail_idx[1] += 1
            elif current_head_idx[1] > len(grid[0]) - 1:
                [row.append(False) for row in grid]
            current_tail_idx = follow(current_head_idx, current_tail_idx)
            grid[current_tail_idx[0]][current_tail_idx[1]] = True

    return sum(x.count(True) for x in grid)


def part_two(moves):
    grid = [[True]]

    # Head in 0, tail in 9
    rope = []
    for i in range(10):
        rope.append([0, 0])

    for move in moves:
        for i in range(move['spaces']):
            move_dir = MOVES[move['dir']]
            prev_move = [0, 0]
            rope[0][0] += move_dir[0]
            rope[0][1] += move_dir[1]

            # Expand the array
            if rope[0][0] < 0:
                grid.insert(0, [False] * len(grid[0]))
                for knot in rope:
                    knot[0] += 1
            elif rope[0][0] > len(grid) - 1:
                grid.append([False] * len(grid[0]))
            elif rope[0][1] < 0:
                [row.insert(0, False) for row in grid]
                for knot in rope:
                    knot[1] += 1
            elif rope[0][1] > len(grid[0]) - 1:
                [row.append(False) for row in grid]
            for idx in range(len(rope)):
                if idx != 0:
                    rope[idx] = follow(rope[idx-1], rope[idx])
                grid[rope[-1][0]][rope[-1][1]] = True

    # thing = [["#" if val else " " for val in row] for row in grid]
    # for idx, r in enumerate(rope):
    #     thing[r[0]][r[1]] = str(idx)
    # print("---")
    # for row in thing:
    #     print(*[value for value in row])
    # print("----")

    return sum(x.count(True) for x in grid)


print(part_one(load_input()))
print(part_two(load_input()))
