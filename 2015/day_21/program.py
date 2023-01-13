from itertools import product

WEAPONS = [
    # Cost, damage, armor
    [8, 4, 0],
    [10, 5, 0],
    [25, 6, 0],
    [40, 7, 0],
    [74, 8, 0],
]

ARMOR = [
    # Cost, damage, armor
    [0, 0, 0],  # For not buying anything
    [13, 0, 1],
    [31, 0, 2],
    [53, 0, 3],
    [75, 0, 4],
    [102, 0, 5]
]

RINGS = [
    [0, 0, 0],  # For not buying anything
    [25, 1, 0],
    [50, 2, 0],
    [100, 3, 0],
    [20, 0, 1],
    [40, 0, 2],
    [80, 0, 3]
]


def get_input():
    with open("day_21/input.txt", "r") as f:
        return list(map(lambda s: int(s.split(" ")[-1]), f.read().splitlines()))


def simulate(boss_damage, boss_armor, boss_hp, damage, armor, hp):
    while hp or boss_hp:
        boss_hp -= damage - boss_armor if damage - boss_armor > 1 else 1
        if boss_hp <= 0:
            return True
        hp -= boss_damage - armor if boss_damage - armor > 1 else 1
        if hp <= 0:
            return False


def part_one(stats):
    hit_points = stats[0]
    damage = stats[1]
    armor = stats[2]
    wins = []
    for combination in product(WEAPONS, ARMOR, RINGS, RINGS):
        if combination[2] == combination[3] != [0, 0, 0]:
            continue
        cost = sum(map(lambda x: x[0], combination))
        total_damage = sum(map(lambda x: x[1], combination))
        total_armor = sum(map(lambda x: x[2], combination))
        if simulate(damage, armor, hit_points, total_damage, total_armor, 100):
            wins.append(cost)

    return min(wins)


def part_two(stats):
    boss_hit_points = stats[0]
    boss_damage = stats[1]
    boss_armor = stats[2]
    losses = []
    for combination in product(WEAPONS, ARMOR, RINGS, RINGS):
        if combination[2] == combination[3] != [0, 0, 0]:
            continue
        cost = sum(map(lambda x: x[0], combination))
        total_damage = sum(map(lambda x: x[1], combination))
        total_armor = sum(map(lambda x: x[2], combination))
        if not simulate(boss_damage, boss_armor, boss_hit_points, total_damage, total_armor, 100):
            losses.append(cost)

    return max(losses)


print(part_one(get_input()))
print(part_two(get_input()))
