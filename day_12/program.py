import curses
from time import sleep
import math
from copy import deepcopy

letters = 'abcdefghijklmnopqrstuvwxyz'


def get_input():
    with open("day_12/input.txt", 'r') as f:
        file: list[str] = f.read().splitlines()
    grid = []
    for row_idx, line in enumerate(file):
        grid.append([])
        for col_idx, char in enumerate(line):
            if char.islower():
                grid[-1].append(letters.index(char))
            elif char == 'S':
                grid[-1].append(0)
                start = (row_idx, col_idx)
            elif char == 'E':
                grid[-1].append(25)
                end = (row_idx, col_idx)
    return grid, start, end


def get_neighbors(grid, point, reverse_neighbor_height=False):
    GRID_ROWS = len(grid)
    GRID_COLS = len(grid[0])
    if not reverse_neighbor_height:
        MAX_HEIGHT = grid[point[0]][point[1]] + 1
    else:
        MIN_HEIGHT = grid[point[0]][point[1]] - 1

    # NOTE: This code might be wrong. I don't think it is but who knows
    point_up = (point[0] - 1, point[1])
    point_down = (point[0] + 1, point[1])
    point_left = (point[0], point[1] - 1)
    point_right = (point[0], point[1] + 1)

    neighbors = []
    if not reverse_neighbor_height:
        if point_up[0] >= 0 and grid[point_up[0]][point_up[1]] <= MAX_HEIGHT:
            neighbors.append(point_up)
        if point_down[0] < GRID_ROWS and grid[point_down[0]][point_down[1]] <= MAX_HEIGHT:
            neighbors.append(point_down)
        if point_left[1] >= 0 and grid[point_left[0]][point_left[1]] <= MAX_HEIGHT:
            neighbors.append(point_left)
        if point_right[1] < GRID_COLS and grid[point_right[0]][point_right[1]] <= MAX_HEIGHT:
            neighbors.append(point_right)
    else:
        if point_up[0] >= 0 and grid[point_up[0]][point_up[1]] >= MIN_HEIGHT:
            neighbors.append(point_up)
        if point_down[0] < GRID_ROWS and grid[point_down[0]][point_down[1]] >= MIN_HEIGHT:
            neighbors.append(point_down)
        if point_left[1] >= 0 and grid[point_left[0]][point_left[1]] >= MIN_HEIGHT:
            neighbors.append(point_left)
        if point_right[1] < GRID_COLS and grid[point_right[0]][point_right[1]] >= MIN_HEIGHT:
            neighbors.append(point_right)

    return neighbors


def dijkstra(grid, start, end, return_all=False, reverse_neighbor_height=False, return_prev=False):
    dist_from_start = [[math.inf for _ in r] for r in grid]
    dist_from_start[start[0]][start[1]] = 0
    visited = []
    unvisited = []
    for row_idx, row in enumerate(grid):
        for col_idx, col in enumerate(row):
            unvisited.append((row_idx, col_idx))
    current_point = start
    prev = [[None for _ in r] for r in grid]

    while unvisited:
        current_neighbors = get_neighbors(
            grid, current_point, reverse_neighbor_height=reverse_neighbor_height)
        for neighbor in current_neighbors:
            # All have size 1
            temp = 1 + \
                dist_from_start[current_point[0]][current_point[1]]
            if temp < dist_from_start[neighbor[0]][neighbor[1]]:
                dist_from_start[neighbor[0]][neighbor[1]] = temp
                prev[neighbor[0]][neighbor[1]] = current_point

        visited.append(current_point)
        del unvisited[unvisited.index(current_point)]
        minimum_d = math.inf
        for item in unvisited:
            if dist_from_start[item[0]][item[1]] < minimum_d:
                current_point = item
                minimum_d = dist_from_start[item[0]][item[1]]
        if minimum_d == math.inf:
            break

    if return_all and return_prev:
        return dist_from_start, prev
    if return_all:
        return dist_from_start

    return dist_from_start[end[0]][end[1]]


def visualize_path(window: curses.window, grid, start, end, max_it=1, delay=0.001):
    curses.curs_set(0)
    d, p = dijkstra(grid, start, end, return_all=True, return_prev=True)
    line = []
    current_point = end
    while current_point:
        line.append(current_point)
        current_point = p[current_point[0]][current_point[1]]
    if line == [end]:
        return
    line.reverse()
    current_idx = 0
    current_up = True
    current_down = False
    current_left = False
    current_right = False
    num_it = 0
    while True:
        if line[current_idx][0] - line[current_idx+1 if current_idx+1 < len(line) else current_idx][0] == 1:
            if not current_up:
                char = "┘" if current_right else "└"
                current_up = True
                current_down = False
                current_left = False
                current_right = False
            else:
                char = "│"
        elif line[current_idx][0] - line[current_idx+1 if current_idx+1 < len(line) else current_idx][0] == -1:
            if not current_down:
                char = "┐" if current_right else "┌"
                current_up = False
                current_down = True
                current_left = False
                current_right = False
            else:
                char = "│"
        elif line[current_idx][1] - line[current_idx+1 if current_idx+1 < len(line) else current_idx][1] == 1:
            if not current_left:
                char = "┐" if current_up else "┘"
                current_up = False
                current_down = False
                current_left = True
                current_right = False
            else:
                char = "─"

        elif line[current_idx][1] - line[current_idx+1 if current_idx+1 < len(line) else current_idx][1] == -1:
            if not current_right:
                char = "┌" if current_up else "└"
                current_up = False
                current_down = False
                current_left = False
                current_right = True
            else:
                char = "─"
        else:
            char = "─"

        window.addch(line[current_idx][0], line[current_idx][1], char)
        window.addch(start[0], start[1], 'S')
        window.addch(end[0], end[1], 'E')
        window.refresh()
        current_idx += 1
        if current_idx == len(line):
            for p in line[::-1]:
                window.addch(p[0], p[1], ' ')
                # window.addch(start[0], start[1], 'S')
                window.addch(end[0], end[1], 'E')
                window.refresh()
                current_idx = 0
                sleep(delay)
            num_it += 1
        sleep(delay)
        if num_it == max_it:
            break


def part_one(grid, start, end):
    return dijkstra(grid, start, end)


def part_two(grid, _, end):
    # This time we're measuring distance from end
    dist_from_start = dijkstra(
        grid, end, None, return_all=True, reverse_neighbor_height=True)

    minimum = math.inf
    for row_idx, row in enumerate(dist_from_start):
        for col_idx, dist in enumerate(row):
            if grid[row_idx][col_idx] == 0 and dist < minimum:
                minimum = dist
    return minimum


def visualize_all():
    grid, start, end = get_input()
    # starts = []
    # for r_idx, row in enumerate(grid):
    #     for c_idx, val in enumerate(row):
    #         if val == 0:
    #             starts.append((r_idx, c_idx))

    # for start in starts:
    curses.wrapper(visualize_path, grid, start, end, delay=0.1)


# visualize_all()

print(part_one(*get_input()))
print(part_two(*get_input()))
