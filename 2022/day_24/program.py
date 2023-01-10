from collections import UserList, defaultdict
import math


class Blizzards(UserList):
    def index_coords(self, index, default=[None, None]):
        for i in self.data:
            if i[0] == index:
                return i
        return default

    def index_in(self, index):
        # return index in [i["loc"] for i in self.data]
        return any(i["loc"] == index for i in self.data)


def get_input():
    with open("day_24/input.txt", "r") as f:
        file = f.read().splitlines()

    # blizzards = [Blizzards()]
    blizzards = [defaultdict(list)]
    for r_idx, row in enumerate(file):
        for c_idx, char in enumerate(row):
            if char != ".":
                # blizzards[0].append([c_idx + r_idx * 1j, char])
                blizzards[0][c_idx + r_idx * 1j] = [char] + \
                    blizzards[0][c_idx + r_idx * 1j]

    return blizzards, len(file), len(file[0])


def gen_time(blizzards, rows, cols):
    i = 0
    while True:
        # blizzards.append(Blizzards())
        blizzards.append(defaultdict(list))

        for blizzard in blizzards[-2]:
            for b in blizzards[-2][blizzard]:
                match b:
                    # match blizzard[1]:
                    case "#":
                        # blizzards[-1].append([blizzard[0], "#"])
                        blizzards[-1][blizzard] = ["#"]
                    case "^":
                        if not (blizzards[-2].get(blizzard - 1j) == ["#"]):
                            # blizzards[-1].append([blizzard[0] - 1j, "^"])
                            blizzards[-1][blizzard - 1j] = ["^"] + \
                                blizzards[-1][blizzard - 1j]
                        else:
                            # blizzards[-1].append([blizzard[0].real +
                            #                     (rows - 1 - 1) * 1j, "^"])
                            blizzards[-1][blizzard.real + (rows - 1 - 1) * 1j] = ["^"] + \
                                blizzards[-1][blizzard.real +
                                              (rows - 1 - 1) * 1j]
                    case ">":
                        if not (blizzards[-2].get(blizzard + 1) == ["#"]):
                            # blizzards[-1].append([blizzard[0] + 1, ">"])
                            blizzards[-1][blizzard + 1] = [">"] + \
                                blizzards[-1][blizzard + 1]
                        else:
                            # blizzards[-1].append([blizzard[0].imag*1j + 1, ">"])
                            blizzards[-1][blizzard.imag*1j + 1] = [">"] + \
                                blizzards[-1][blizzard.imag*1j + 1]
                    case "v":
                        if not (blizzards[-2].get(blizzard + 1j) == ["#"]):
                            # blizzards[-1].append([blizzard[0] + 1j, "v"])
                            blizzards[-1][blizzard + 1j] = ["v"] + \
                                blizzards[-1][blizzard + 1j]
                        else:
                            # blizzards[-1].append([blizzard[0].real + 1j, "v"])
                            blizzards[-1][blizzard.real + 1j] = ["v"] + \
                                blizzards[-1][blizzard.real + 1j]
                    case "<":
                        if not (blizzards[-2].get(blizzard - 1) == ["#"]):
                            # blizzards[-1].append([blizzard[0] - 1, "<"])
                            blizzards[-1][blizzard - 1] = ["<"] + \
                                blizzards[-1][blizzard - 1]
                        else:
                            # blizzards[-1].append([blizzard[0].imag *
                            #                       1j + cols - 2, "<"])
                            blizzards[-1][blizzard.imag * 1j + cols - 2] = ["<"] + \
                                blizzards[-1][blizzard.imag * 1j + cols - 2]
        i += 1
        if blizzards[i] == blizzards[0] and i != 1:
            del blizzards[i]
            break


def dijkstra(blizzards, start, end, rows, cols, initial_depth=0, reverse=False):
    if reverse:
        start, end = end, start
    dist_from_start = [{
        c+r*1j: math.inf for c in range(cols) for r in range(rows)}]
    queue = []
    dist_from_start[0][start] = 0
    visited = []
    unvisited = []
    for col_idx in range(cols):
        for row_idx in range(rows):
            # for depth in range(500):
            if row_idx * 1j + col_idx not in blizzards[0]:
                unvisited.append((row_idx * 1j + col_idx, 0))
    current_point = (start, initial_depth)
    prev = [{c+r*1j: None for c in range(cols)
             for r in range(rows)}]

    while unvisited:
        current_neighbors = []
        while 5+current_point[1] > len(dist_from_start):
            for col_idx in range(cols):
                for row_idx in range(rows):
                    if row_idx * 1j + col_idx not in blizzards[(1+current_point[1]) % len(blizzards)]:
                        unvisited.append(
                            (row_idx * 1j + col_idx, 1+current_point[1]))
                        dist_from_start.append(
                            {c+r*1j: math.inf for c in range(cols) for r in range(rows)})
                        prev.append(
                            {c+r*1j: None for c in range(cols) for r in range(rows)})
        for dir in [1, -1, 1j, -1j, 0]:
            if current_point[0] + dir not in blizzards[(1+current_point[1]) % len(blizzards)] and cols > (current_point[0] + dir).real >= 0 and rows > (current_point[0] + dir).imag >= 0:
                current_neighbors.append(
                    (current_point[0] + dir, (1+current_point[1])))
        for neighbor in current_neighbors:
            queue.append(neighbor)
            # All have size 1
            temp = 1 + \
                current_point[1]
            if temp < dist_from_start[neighbor[1]][neighbor[0]]:
                dist_from_start[neighbor[1]][neighbor[0]] = temp
                prev[neighbor[1]][neighbor[0]] = current_point

        visited.append(current_point)
        try:
            del unvisited[unvisited.index(current_point)]
        except ValueError:
            pass
        queue = list(dict.fromkeys(queue))
        current_point = queue.pop(0)
        if current_point[0] == end:
            break

    for idx, layer in enumerate(dist_from_start):
        if layer[end] != math.inf:
            return idx


def part_one(blizzards, rows, cols):
    gen_time(blizzards, rows, cols)
    return dijkstra(blizzards, 1+0j, cols - 2 + (rows - 1) * 1j, rows, cols)


def part_two(blizzards, rows, cols):
    gen_time(blizzards, rows, cols)
    there = dijkstra(blizzards, 1+0j, cols - 2 + (rows - 1) * 1j, rows, cols)
    back = dijkstra(blizzards, 1+0j, cols - 2 + (rows - 1) * 1j,
                    rows, cols, reverse=True, initial_depth=there)
    again = dijkstra(blizzards, 1+0j, cols - 2 + (rows - 1)
                     * 1j, rows, cols, initial_depth=back)
    return again


print(part_one(*get_input()))
print(part_two(*get_input()))
