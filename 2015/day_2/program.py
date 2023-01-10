def get_input():
    with open("day_2/input.txt", "r") as f:
        file = f.read().splitlines()

    dimension_tuples = []
    for line in file:
        dimension_tuples.append(tuple(map(int, line.split("x"))))

    return dimension_tuples


def part_one(dimensions):
    def gen_sides(rect): return [rect[0]*rect[1],
                                 rect[1]*rect[2], rect[0]*rect[2]]

    def wrapping(rect): return min(gen_sides(rect)) + \
        sum(map(lambda x: x*2, gen_sides(rect)))

    return sum(map(wrapping, dimensions))


def part_two(dimensions):
    def perimeters(rect): return [2*(rect[0]+rect[1]),
                                  2*(rect[1]+rect[2]), 2*(rect[0]+rect[2])]

    def ribbon(rect): return min(perimeters(rect)) + rect[0]*rect[1]*rect[2]
    return sum(map(ribbon, dimensions))


print(part_one(get_input()))
print(part_two(get_input()))
