import math
from collections import defaultdict
from copy import deepcopy
import itertools


def get_input():
    with open("day_16/input.txt", "r") as f:
        file = f.read().splitlines()

    valves = {}
    for valve in file:
        valves[valve.split(" ")[1]] = {
            "flow_rate": int(valve.replace(";", "=").split("=")[1]),
            "neighbors": valve.replace(",", "").split(" ")[9:],
            "discovered": False
        }

    return valves


def dfs(valves, weights, start, length, paths, path=[], open_valve=False, depth=0):
    if depth > length:
        valve_bits = {valve: 1 << i for i, valve in enumerate(valves.keys())}
        valve_bits["AA"] = 0
        paths.append(
            {"path": path, "open_valves": sum([valve_bits[p["node"]] for p in path])})
        return
    path = path + \
        [{"node": start, "valve_opening": open_valve, "depth": depth}]
    for valve in weights:
        if valve == start:
            continue
        if valves[valve]["flow_rate"] > 0 and valve not in [p["node"] for p in path]:
            dfs(valves, weights, valve, length,
                paths, deepcopy(path), open_valve=True, depth=depth + weights[start][valve] + 1)


def warshall(valves, start="AA"):
    dist = {}
    for v in valves:
        dist[v] = {}
    for v in valves:
        for node in valves:
            if node in valves[v]["neighbors"]:
                dist[v][node] = 1
            else:
                dist[v][node] = math.inf
        dist[v][v] = 0

    for k in valves:
        for i in valves:
            for j in valves:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


def part_one(valves):
    paths = []
    dist = warshall(valves)
    valid_valves = [
        valve for valve in valves if valves[valve]["flow_rate"] > 0 or valve == "AA"]

    to_del = []
    for d in dist:
        if d not in valid_valves:
            to_del.append(d)

    for item in to_del:
        del dist[item]

    to_del = []
    for d in dist:
        for s in dist[d]:
            if not s in valid_valves:
                to_del.append((d, s))

    for item in to_del:
        del dist[item[0]][item[1]]

    dfs(valves, dist, "AA", 30, paths)
    pressures = []
    for path in paths:
        path = path["path"]
        has_dups = len(set([node["node"] for node in path])) != len(
            [node["node"] for node in path])
        if has_dups:
            continue
        pressure = 0
        for idx, node in enumerate(path):
            if node["valve_opening"]:
                pressure += (30-node["depth"]) * \
                    valves[node["node"]]["flow_rate"]
        pressures.append(pressure)
    return max(pressures)


def part_two(valves):
    dist = warshall(valves)
    valid_valves = [
        valve for valve in valves if valves[valve]["flow_rate"] > 0 or valve == "AA"]

    to_del = []
    for d in dist:
        if d not in valid_valves:
            to_del.append(d)

    for item in to_del:
        del dist[item]

    to_del = []
    for d in dist:
        for s in dist[d]:
            if not s in valid_valves:
                to_del.append((d, s))

    for item in to_del:
        del dist[item[0]][item[1]]

    h_paths = []
    paths_by_opened = defaultdict(list)
    dfs(valves, dist, "AA", 26, h_paths)
    new_h_paths = []

    pressures = []

    for h_path in h_paths:
        path = h_path["path"]
        has_dups = len(set([node["node"] for node in path])) != len(
            [node["node"] for node in path])
        if has_dups:
            continue
        pressure = 0
        for idx, node in enumerate(path):
            if node["valve_opening"]:
                pressure += (26-node["depth"]) * \
                    valves[node["node"]]["flow_rate"]
        new_h_paths.append({"pressure": pressure, "path": path,
                           "open_valves": h_path["open_valves"]})

    paths = sorted(new_h_paths, key=lambda x: x["pressure"], reverse=True)
    for path in paths:
        paths_by_opened[path["open_valves"]].append(path)

    max_path_by_opened = {}
    for key, path_set in paths_by_opened.items():
        max_path_by_opened[key] = max([p["pressure"] for p in path_set])
    return max(h_pressure + e_pressure for (h_open_valves, h_pressure), (e_open_valves, e_pressure) in itertools.combinations(max_path_by_opened.items(), 2) if not h_open_valves & e_open_valves)


print(part_one(get_input()))
print(part_two(get_input()))
