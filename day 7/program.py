import copy


def get_input():
    with open("day 7/input.txt", "r") as f:
        return f.readlines()


def access_dict(dict, dir_keys):
    val = dict
    for key in dir_keys:
        val = val[key]

    return val


def gen_fs(file: list[str]):
    fs = {}  # Directories are name: dict. files are name: size[int]
    current_dir_keys = []
    current_dict = fs

    for line in file:
        line = line.strip()
        if line.startswith("$ cd"):
            dir = line.split("$ cd ")[1]
            if dir != ".." and dir != '/':
                current_dir_keys.append(dir)

                if not dir in current_dict:
                    current_dict[dir] = {}
                current_dict = access_dict(current_dict, [dir])
            elif dir != '/':
                del current_dir_keys[-1]
                current_dict = access_dict(fs, current_dir_keys)
            else:
                current_dir_keys = []
                current_dict = fs
        elif not line.startswith("$ ls"):
            dir_or_size, fname = line.split(' ')
            if dir_or_size == "dir":
                current_dict[fname] = {}
            else:
                current_dict[fname] = int(dir_or_size)
    return fs


def size_of_dir(dict):
    size = 0
    # print(str(dict))
    for key, value in dict.items():
        if isinstance(value, int):
            size += value
        elif not isinstance(value, int):
            size += size_of_dir(value)
    # print(size, dict)
    return size


def walk_dict_part_one(dict, root=True):
    total_less_100k = 0
    if root:
        total_size = size_of_dir(dict)
        if total_size <= 100_000:
            total_less_100k += total_size
    for key, value in dict.items():
        if not isinstance(value, int):
            size = size_of_dir(value)
            if size <= 100_000:
                total_less_100k += size
            total_less_100k += walk_dict_part_one(value, root=False)

    return total_less_100k


def walk_dict_part_two(dict, space_to_free, lowest_space=70_000_001):
    for key, value in dict.items():
        if not isinstance(value, int):
            size = size_of_dir(value)
            if size >= space_to_free and size < lowest_space:
                lowest_space = size
            lowest_space = walk_dict_part_two(
                value, space_to_free, lowest_space=lowest_space,)
    return lowest_space


def part_one(file: list[str]):
    fs = gen_fs(file)

    print(walk_dict_part_one(fs))


def part_two(file: list[str]):
    TOTAL_SPACE = 70_000_000
    SPACE_REQUIRED = 30_000_000
    fs = gen_fs(file)
    space_used = size_of_dir(fs)
    space_to_free = SPACE_REQUIRED - (TOTAL_SPACE - space_used)

    print(walk_dict_part_two(fs, space_to_free))


part_one(get_input())
part_two(get_input())
