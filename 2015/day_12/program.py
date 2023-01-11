from json import loads


def get_input():
    with open("day_12/input.txt", "r") as f:
        file = f.read()

    return loads(file)


def proc_json(json, p2=False):
    if isinstance(json, list):
        return sum(proc_json(item, p2=p2) for item in json)
    elif isinstance(json, dict):
        if "red" in json.values() and p2:
            return 0
        return sum(proc_json(item, p2=p2) for item in json.values())
    elif isinstance(json, int):
        return json
    else:
        return 0


def part_one(json):
    return proc_json(json)


def part_two(json):
    return proc_json(json, p2=True)


print(part_one(get_input()))
print(part_two(get_input()))
