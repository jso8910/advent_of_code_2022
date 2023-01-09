def get_input():
    with open("day_25/input.txt", "r") as f:
        file = f.read().splitlines()
    return file


def snafu_to_dec(num):
    number = 0
    for idx, char in enumerate(num[::-1]):
        match char:
            case "0":
                number += 0
            case "1":
                number += 5 ** idx
            case "2":
                number += 2 * 5 ** idx
            case "-":
                number -= 5 ** idx
            case "=":
                number -= 2 * 5 ** idx

    return number


def dec_to_snafu(num):
    snafu = []
    while num != 0:
        dig = num % 5
        if dig == 0:
            snafu.append("0")
        elif dig == 1:
            snafu.append("1")
        elif dig == 2:
            snafu.append("2")
        elif dig == 3:
            snafu.append("=")
        elif dig == 4:
            snafu.append("-")
        elif dig == 5:
            snafu.append("0")
        num = (num + 2) // 5
    return "".join(snafu[::-1])


def part_one(nums):
    s = 0
    for num in nums:
        s += snafu_to_dec(num)
    return dec_to_snafu(s)


print(part_one(get_input()))
