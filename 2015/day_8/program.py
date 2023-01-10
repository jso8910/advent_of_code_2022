import re


def get_input():
    with open("day_8/input.txt", "r") as f:
        file = f.read().splitlines()

    return file


def part_one(strings):

    total_code_chars = sum(map(len, strings))
    total_mem_chars = sum(map(len, map(eval, strings)))

    return total_code_chars - total_mem_chars


def part_two(strings):
    def new_string(string):
        string = string.replace('\\', '\\\\')
        string = string.replace('"', '\\"')
        string = '"' + string + '"'
        return string

    total_code_chars_new = sum(map(len, map(new_string, strings)))
    total_code_chars = sum(map(len, strings))

    return total_code_chars_new - total_code_chars


print(part_one(get_input()))
print(part_two(get_input()))
