def part_one():
    with open("day_2/input.txt", "r") as f:
        file = f.readlines()
    strategy: list[tuple[str, str]] = []

    translator = {"A": "R", "B": "P", "C": "S", "X": "R", "Y": "P", "Z": "S"}

    lookups = {"win": {"R": "P", "P": "S", "S": "R"},
               "loss": {"R": "S", "P": "R", "S": "P"}}

    for line in file:
        opponent_choice = translator[line.split(" ")[0]]
        player_choice = translator[line.split(" ")[1].strip()]
        strategy.append((opponent_choice, player_choice))

    points = {"R": 1, "P": 2, "S": 3}
    total_points = 0
    for strat in strategy:
        total_points += points[strat[1]]
        if strat[0] == strat[1]:
            total_points += 3
        elif strat[0] == "R" and strat[1] == "P":
            total_points += 6
        elif strat[0] == "P" and strat[1] == "S":
            total_points += 6
        elif strat[0] == "S" and strat[1] == "R":
            total_points += 6

    return total_points


def part_two():
    with open("day_2/input.txt", "r") as f:
        file = f.readlines()
    strategy: list[tuple[str, str]] = []

    translator = {"A": "R", "B": "P", "C": "S"}

    lookups = {"win": {"R": "P", "P": "S", "S": "R"},
               "loss": {"R": "S", "P": "R", "S": "P"}}
    points = {"R": 1, "P": 2, "S": 3}
    total_points = 0
    for line in file:
        opponent_choice = translator[line.split(" ")[0]]
        player_result = line.split(" ")[1].strip()
        if player_result == "X":  # Loss
            strategy.append(
                (opponent_choice, lookups['loss'][opponent_choice]))
            total_points += points[lookups['loss'][opponent_choice]]
        elif player_result == "Z":  # Win
            strategy.append((opponent_choice, lookups['win'][opponent_choice]))
            total_points += points[lookups['win'][opponent_choice]]
            total_points += 6
        else:
            strategy.append((opponent_choice, opponent_choice))
            total_points += points[opponent_choice]
            total_points += 3

    return total_points


print(part_one())
print(part_two())
