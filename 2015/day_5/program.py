from collections import Counter


def get_input():
    with open("day_5/input.txt", "r") as f:
        file = f.read().splitlines()

    return file


def double_letters(word, p_2=False):
    for i in range(len(word)-1-p_2):
        if word[i] == word[i+1+p_2]:
            return True
    return False


def pair_repeat(word):
    for i in range(len(word)-3):
        sub = word[i:i+2]
        if sub in word[i+2:]:
            return True


def part_one(words):
    def is_nice(word):
        vowels = "aeiou"
        if not len([letter for letter in word if letter in vowels]) >= 3:
            return False
        if not double_letters(word):
            return False
        if any(map(word.__contains__, ["ab", "cd", "pq", "xy"])):
            return False

        return True

    return sum(map(is_nice, words))


def part_two(words):
    def is_nice(word):
        if not pair_repeat(word):
            return False
        if not double_letters(word, p_2=True):
            return False

        return True

    return sum(map(is_nice, words))


print(part_one(get_input()))
print(part_two(get_input()))
