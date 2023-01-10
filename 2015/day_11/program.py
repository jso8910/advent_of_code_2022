def get_input():
    with open("day_11/input.txt", "r") as f:
        return f.read()


def password_valid(password):
    if len(password) != 8:
        return False

    if any(c in password for c in "iol"):
        return False

    triplets = []
    for triplet in zip(password, password[1:], password[2:]):
        triplets.append(ord(triplet[2]) - ord(triplet[1])
                        == ord(triplet[1]) - ord(triplet[0]) == 1)

    if not any(triplets):
        return False

    pairs = set()
    for pair in zip(password, password[1:]):
        if pair[0] == pair[1]:
            pairs.add(pair)

    if len(pairs) < 2:
        return False

    return True


def inc_pass(password):
    num_inced = False
    digit = -1
    while not num_inced:
        # if abs(digit) > len(password):
        #     password = "a" + password
        #     num_inced = True
        if password[digit] == "z":
            password = list(password)
            password[digit] = "a"
            password = "".join(password)
            digit -= 1
        else:
            # password[digit] = chr(ord(password[digit]) + 1)
            password = list(password)
            password[digit] = chr(ord(password[digit]) + 1)
            password = "".join(password)
            num_inced = True

    return password


def part_one(password):
    while not password_valid(password):
        password = inc_pass(password)

    return password


print(part_one(get_input()))
# Honestly I couldn't be bothered to make a second solution function since this was so easy
print(part_one(inc_pass(part_one(get_input()))))
