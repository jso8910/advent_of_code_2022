import re


def get_input():
    with open("day_14/input.txt", "r") as f:
        file = f.read().splitlines()

    prog = re.compile(
        r"(\b[a-zA-Z]+\b) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.")
    reindeer = {}
    for line in file:
        match = prog.match(line)
        if match:
            name = match.group(1)
            speed = int(match.group(2))
            fly_time = int(match.group(3))
            rest_time = int(match.group(4))
            reindeer[name] = (speed, fly_time, rest_time)

    return reindeer


def part_one(reindeer):
    state = {key: {"dist": 0, "time": 0, "rest_needed": False}
             for key in reindeer.keys()}
    for i in range(2503):
        for name, (speed, fly_time, rest_time) in reindeer.items():
            if state[name]["rest_needed"]:
                state[name]["time"] += 1
                if state[name]["time"] == rest_time:
                    state[name]["rest_needed"] = False
                    state[name]["time"] = 0
            else:
                state[name]["dist"] += speed
                state[name]["time"] += 1
                if state[name]["time"] == fly_time:
                    state[name]["rest_needed"] = True
                    state[name]["time"] = 0

    return max(state.values(), key=lambda x: x["dist"])["dist"]


def part_two(reindeer):
    state = {key: {"dist": 0, "time": 0, "rest_needed": False, "points": 0}
             for key in reindeer.keys()}
    for i in range(2503):
        for name, (speed, fly_time, rest_time) in reindeer.items():
            if state[name]["rest_needed"]:
                state[name]["time"] += 1
                if state[name]["time"] == rest_time:
                    state[name]["rest_needed"] = False
                    state[name]["time"] = 0
            else:
                state[name]["dist"] += speed
                state[name]["time"] += 1
                if state[name]["time"] == fly_time:
                    state[name]["rest_needed"] = True
                    state[name]["time"] = 0
        max_val = max(state.values(), key=lambda x: x["dist"])["dist"]
        i = 0
        for val in state.values():
            if val["dist"] == max_val:
                val["points"] += 1

    return max(state.values(), key=lambda x: x["points"])["points"]


print(part_one(get_input()))
print(part_two(get_input()))
