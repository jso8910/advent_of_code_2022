import functools
import re
from copy import deepcopy

INITIAL_STATE = {
    "machines": {
        "ore": 1,
        "clay": 0,
        "obsidian": 0,
        "geode": 0
    },
    "resources": {
        "ore": 0,
        "clay": 0,
        "obsidian": 0,
        "geode": 0
    }
}


def get_input():
    with open("day_19/input.txt", "r") as f:
        file = f.read().splitlines()

    prog = re.compile(r"Blueprint (\d+): Each ore robot costs (\d+) ore\. "
                      r"Each clay robot costs (\d+) ore\. Each obsidian robot "
                      r"costs (\d+) ore and (\d+) clay\. Each geode robot costs (\d+) ore and (\d+) obsidian\.")

    blueprints = []
    for line in file:
        blueprint = {}
        match = prog.match(line)
        if match:
            blueprint["id"] = int(match.group(1))
            blueprint["ore"] = int(match.group(2))
            blueprint["clay"] = int(match.group(3))
            blueprint["obsidian"] = {}
            blueprint["obsidian"]["ore"] = int(match.group(4))
            blueprint["obsidian"]["clay"] = int(match.group(5))
            blueprint["geode"] = {}
            blueprint["geode"]["ore"] = int(match.group(6))
            blueprint["geode"]["obsidian"] = int(match.group(7))

            blueprints.append(blueprint)

    return blueprints


scenarios = []


def dfs(blueprint, state=deepcopy(INITIAL_STATE), length=24, length_in=1):
    global scenarios
    if length_in > length:
        scenarios.append(state)
        return

    choices = ["none"]
    if state["resources"]["ore"] >= blueprint["ore"]:
        # It's never efficient to build it if you could've built it last time
        if state["resources"]["ore"] - state["machines"]["ore"] < blueprint["ore"]:
            # Don't build too many ore robots per minute
            if state["machines"]["ore"] + 1 <= max([blueprint["clay"], blueprint["obsidian"]["ore"], blueprint["geode"]["ore"]]):
                choices.append("ore")
    if state["resources"]["ore"] >= blueprint["clay"]:
        # It's never efficient to build it if you could've built it last time
        if state["resources"]["ore"] - state["machines"]["ore"] < blueprint["clay"]:
            # Don't build too many clay robots per minute
            if state["machines"]["clay"] + 1 <= blueprint["obsidian"]["clay"]:
                choices.append("clay")
    if state["resources"]["ore"] >= blueprint["obsidian"]["ore"] and state["resources"]["clay"] >= blueprint["obsidian"]["clay"]:
        # Don't build too many obsidian robots per minute
        if state["machines"]["obsidian"] + 1 <= blueprint["geode"]["obsidian"]:
            choices = ["obsidian", "none"]
    if state["resources"]["ore"] >= blueprint["geode"]["ore"] and state["resources"]["obsidian"] >= blueprint["geode"]["obsidian"]:
        # Always build geode robot if possible
        choices = ["geode"]

    for choice in choices:
        n_state = deepcopy(state)
        n_state["resources"]["ore"] += n_state["machines"]["ore"]
        n_state["resources"]["clay"] += n_state["machines"]["clay"]
        n_state["resources"]["obsidian"] += n_state["machines"]["obsidian"]
        n_state["resources"]["geode"] += n_state["machines"]["geode"]
        if choice == "none":
            dfs(blueprint, state=n_state,
                length=length, length_in=length_in+1)
        elif choice == "ore":
            n_state["resources"]["ore"] -= blueprint["ore"]
            n_state["machines"]["ore"] += 1
            dfs(blueprint, state=n_state,
                length=length, length_in=length_in+1)
        elif choice == "clay":
            n_state["resources"]["ore"] -= blueprint["clay"]
            n_state["machines"]["clay"] += 1
            dfs(blueprint, state=n_state,
                length=length, length_in=length_in+1)
        elif choice == "obsidian":
            n_state["resources"]["ore"] -= blueprint["obsidian"]["ore"]
            n_state["resources"]["clay"] -= blueprint["obsidian"]["clay"]
            n_state["machines"]["obsidian"] += 1
            dfs(blueprint, state=n_state,
                length=length, length_in=length_in+1)
        elif choice == "geode":
            n_state["resources"]["ore"] -= blueprint["geode"]["ore"]
            n_state["resources"]["obsidian"] -= blueprint["geode"]["obsidian"]
            n_state["machines"]["geode"] += 1
            dfs(blueprint, state=n_state,
                length=length, length_in=length_in+1)


def part_one(blueprints):
    global scenarios
    blueprint_results = []
    for blueprint in blueprints:
        scenarios = []
        dfs(blueprint)
        blueprint_results.append(scenarios)

    quality_sum = 0
    for idx, bp in enumerate(blueprint_results):
        max_bp = sorted(
            bp, key=lambda x: x["resources"]["geode"], reverse=True)[0]

        quality_sum += (idx + 1) * max_bp["resources"]["geode"]
    return quality_sum


def part_two(blueprints):
    global scenarios
    blueprint_results = []
    for blueprint in blueprints[:3]:
        scenarios = []
        dfs(blueprint, length=32)
        blueprint_results.append(scenarios)

    quality_sum = 1
    for idx, bp in enumerate(blueprint_results):
        max_bp = sorted(
            bp, key=lambda x: x["resources"]["geode"], reverse=True)[0]

        quality_sum *= max_bp["resources"]["geode"]
    return quality_sum


print(part_one(get_input()))
print(part_two(get_input()))
