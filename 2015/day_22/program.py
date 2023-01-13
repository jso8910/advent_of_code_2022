from math import inf
from copy import deepcopy

SPELLS = [
    # Cost, damage, heal, armor, mana, length
    [53, 4, 0, 0, 0, 1],
    [73, 2, 2, 0, 0, 1],
    [113, 0, 0, 7, 0, 6],
    [173, 3, 0, 0, 0, 6],
    [229, 0, 0, 0, 101, 5]
]


def get_input():
    with open("day_22/input.txt", "r") as f:
        return list(map(lambda s: int(s.split(" ")[-1]), f.read().splitlines()))


def simulate(spell, boss_hp, player_hp, boss_damage, current_mana, mana_spent, effects, wins, visited_states, part_2=False):
    assert all(x >= 0 for xs in effects for x in xs), effects
    if len(visited_states) % 5000 == 0:
        print(len(visited_states))

    visited_states.append((boss_hp, player_hp, current_mana,
                           str(effects)))
    shield = 0
    if spell[0:5] in [e[0:5] for e in effects if e[5] > 1]:
        return
    current_mana -= spell[0]
    mana_spent += spell[0]
    if current_mana < 0 or mana_spent >= min(wins):
        return
    player_hp -= part_2
    boss_hp -= sum(map(lambda x: x[1], effects))
    player_hp += sum(map(lambda x: x[2], effects))
    shield += sum(map(lambda x: x[3], effects))
    current_mana += sum(map(lambda x: x[4], effects))

    for idx, effect in enumerate(effects):
        effect[5] -= 1
    effects = [e for e in effects if e[5] > 0]
    if spell[5] > 1:
        effects.append(deepcopy(spell))
    else:
        boss_hp -= spell[1]
        player_hp += spell[2]
        shield += spell[3]
        current_mana += spell[4]

    if boss_hp <= 0:
        wins.append(mana_spent)
        return
    elif player_hp <= 0:
        return

    shield = 0
    current_mana += sum(map(lambda x: x[4], effects))
    boss_hp -= sum(map(lambda x: x[1], effects))
    player_hp += sum(map(lambda x: x[2], effects))
    shield += sum(map(lambda x: x[3], effects))
    for idx, effect in enumerate(effects):
        effect[5] -= 1

    effects = [e for e in effects if e[5] > 0]

    if boss_damage - shield <= 0:
        player_hp -= 1
    else:
        player_hp -= boss_damage - shield

    if boss_hp <= 0:
        wins.append(mana_spent)
        return
    elif player_hp <= 0:
        return

    for spell in SPELLS:
        simulate(deepcopy(spell), boss_hp, player_hp, boss_damage, current_mana,
                 mana_spent, deepcopy(effects), wins, visited_states, part_2=part_2)


def part_one(boss_hp, boss_damage):
    wins = [inf]
    states = []
    for spell in SPELLS:
        simulate(deepcopy(spell), boss_hp, 50, boss_damage, 500,
                 0, deepcopy([]), wins, states)

    return min(wins)


def part_two(boss_hp, boss_damage):
    wins = [inf]
    states = []
    for spell in SPELLS:
        simulate(deepcopy(spell), boss_hp, 50, boss_damage, 500,
                 0, deepcopy([]), wins, states, part_2=True)

    return min(wins)


print(part_one(*get_input()))
print(part_two(*get_input()))
