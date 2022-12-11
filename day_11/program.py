from math import lcm


class Monkey:
    def __init__(self, input: list[str]):
        # -1 to get rid of the last character which is a colon
        self.id = str(input[0].split(' ')[1][:-1])
        self.items = [int(i.strip())
                      for i in input[1].split(":")[1].split(',')]
        self.new = lambda old: eval(input[2].split("= ")[1])
        self.test = lambda item: item % int(input[3].split(' ')[-1]) == 0
        self.divisor = int(input[3].split(' ')[-1])
        self.throw_true = int(input[4].split(' ')[-1])
        self.throw_false = int(input[5].split(' ')[-1])
        self.num_inspected = 0

    def __repr__(self):
        return f"<Monkey object id={self.id}>"
    # def execute_round(self):
    #     self.items[0] = self.new(self.items[0])
    #     self.items[0] //= 3


def get_input():
    with open("day_11/input.txt", "r") as f:
        file = [monkey.splitlines() for monkey in f.read().split("\n\n")]

    return file


def part_one(monkeys_in: list[list[str]]):
    monkeys: list[Monkey] = []
    for monkey in monkeys_in:
        monkeys.append(Monkey(monkey))

    monkeys = sorted(monkeys, key=lambda x: x.id)
    for _ in range(20):
        for monkey in monkeys:
            for item in monkey.items:
                item = monkey.new(item)
                item //= 3
                if monkey.test(item):
                    monkeys[monkey.throw_true].items.insert(0, item)
                else:
                    monkeys[monkey.throw_false].items.insert(0, item)
                monkey.num_inspected += 1
            monkey.items = []

    monkeys_sorted_inspected = sorted(
        monkeys, key=lambda x: x.num_inspected, reverse=True)
    return monkeys_sorted_inspected[0].num_inspected * monkeys_sorted_inspected[1].num_inspected


def part_two(monkeys_in: list[list[str]]):
    monkeys: list[Monkey] = []
    for monkey in monkeys_in:
        monkeys.append(Monkey(monkey))

    monkeys = sorted(monkeys, key=lambda x: x.id)
    divisors = []
    for monkey in monkeys:
        divisors.append(monkey.divisor)

    l = lcm(*divisors)
    for _ in range(10000):
        for monkey in monkeys:
            while monkey.items:
                monkey.items[0] = monkey.new(monkey.items[0])
                monkey.items[0] = monkey.items[0] % l
                if monkey.test(monkey.items[0]):
                    monkeys[monkey.throw_true].items.insert(
                        0, monkey.items.pop(0))
                else:
                    monkeys[monkey.throw_false].items.insert(
                        0, monkey.items.pop(0))
                monkey.num_inspected += 1
            # for item in monkey.items:
            #     item = monkey.new(item)
            #     if monkey.test(item):
            #         monkeys[monkey.throw_true].items.insert(0, item)
            #     else:
            #         monkeys[monkey.throw_false].items.insert(0, item)
            #     monkey.num_inspected += 1
            # monkey.items = []

    monkeys_sorted_inspected = sorted(
        monkeys, key=lambda x: x.num_inspected, reverse=True)
    return monkeys_sorted_inspected[0].num_inspected * monkeys_sorted_inspected[1].num_inspected


print(part_one(get_input()))
print(part_two(get_input()))
