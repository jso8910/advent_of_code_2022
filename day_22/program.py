size = 50


def get_input(part_2=False):
    with open("day_22/input.txt", "r") as f:
        temp = f.read().split("\n\n")
        file = [temp[0].splitlines(), temp[1]]

    grid = {}
    top_left = 0
    for row, line in enumerate(file[0]):
        for col, char in enumerate(line):
            if char == ".":
                grid[col + row * 1j] = True
                if row == 0 and not top_left:
                    top_left = col + row * 1j
            elif char == "#":
                grid[col + row * 1j] = False

    instructions = []
    current_dir = 1
    temp = ""
    for char in file[1]:
        if char.isdigit():
            temp += char
        elif temp and not char.isdigit() and not part_2:
            instructions.append(int(temp) * current_dir)
            # print(int(temp), current_dir, char)
            temp = ""
            if char == "L":
                if current_dir == -1:
                    current_dir = 1j
                elif current_dir == 1j:
                    current_dir = 1
                elif current_dir == 1:
                    current_dir = -1j
                elif current_dir == -1j:
                    current_dir = -1
            elif char == "R":
                if current_dir == -1:
                    current_dir = -1j
                elif current_dir == -1j:
                    current_dir = 1
                elif current_dir == 1:
                    current_dir = 1j
                elif current_dir == 1j:
                    current_dir = -1
        elif temp and not char.isdigit() and part_2:
            instructions.append(int(temp))
            instructions.append(char)
            temp = ""

    if temp:
        instructions.append(int(temp) * current_dir)

    prev_ins = ""
    for instruction in instructions:
        if type(instruction) == type(prev_ins):
            print(instruction, prev_ins)
            raise AssertionError
        prev_ins = instruction

    return grid, top_left, instructions


def gen_wrap_cube_example(grid, start_point, size=50):
    # NOTE: This only works for the example
    global edges_1, edges_2, edges_3, edges_4, edges_5, edges_6
    # I am not going to try to explain these comprehensions other than it was hell to write that took me an hour
    top_1 = [(p + start_point.real) + 0j for p in range(size)]
    left_1 = [start_point.real + p * 1j for p in range(size)]
    right_1 = [start_point.real + size-1 + p * 1j for p in range(size)]
    bottom_1 = [(p + start_point.real) + size * 1j-1j for p in range(size)]
    edges_1 = top_1 + left_1 + right_1 + bottom_1

    top_2 = [(p + start_point.real) + size * 1j for p in range(size)]
    left_2 = [start_point.real + (size + p) * 1j for p in range(size)]
    right_2 = [start_point.real + size-1 +
               (size + p) * 1j for p in range(size)]
    bottom_2 = [(p + start_point.real) + size * 2j-1j for p in range(size)]
    edges_2 = top_2 + left_2 + right_2 + bottom_2

    top_3 = [(p + start_point.real) + size * 2j for p in range(size)]
    left_3 = [start_point.real + (size*2 + p) * 1j for p in range(size)]
    right_3 = [start_point.real + size-1 +
               (size*2 + p) * 1j for p in range(size)]
    bottom_3 = [(p + start_point.real) + size * 3j-1j for p in range(size)]
    edges_3 = top_3 + left_3 + right_3 + bottom_3

    top_4 = [(p + start_point.real)-2*size + size * 1j for p in range(size)]
    left_4 = [start_point.real-2*size +
              (size + p) * 1j for p in range(size)]
    right_4 = [start_point.real-2*size + size-1 +
               (size + p) * 1j for p in range(size)]
    bottom_4 = [(p + start_point.real)-2*size +
                size * 2j-1j for p in range(size)]
    edges_4 = top_4 + left_4 + right_4 + bottom_4

    top_5 = [(p + start_point.real)-size + size * 1j for p in range(size)]
    left_5 = [start_point.real-size +
              (size + p) * 1j for p in range(size)]
    right_5 = [start_point.real-size + size-1 +
               (size + p) * 1j for p in range(size)]
    bottom_5 = [(p + start_point.real)-size +
                size * 2j-1j for p in range(size)]
    edges_5 = top_5 + left_5 + right_5 + bottom_5

    top_6 = [(p + start_point.real) + size + size * 2j for p in range(size)]
    left_6 = [start_point.real + size + (size*2 + p) * 1j for p in range(size)]
    right_6 = [start_point.real + 2*size-1 +
               (size*2 + p) * 1j for p in range(size)]
    bottom_6 = [(p + start_point.real) + size +
                size * 3j-1j for p in range(size)]
    edges_6 = top_6 + left_6 + right_6 + bottom_6
    """
        1
    4 5 2
        3 6
    Adjacent sides:
    - Top of 1 and top of 4
    - Bottom of 1 and top of 2
    - Left of 1 and top of 5
    - Right of 1 and right of 6
    - Left of 2 and right of 5
    - Right of 2 and top of 6
    - Bottom of 2 and top of 3
    - Left of 3 and bottom of 5
    - Right of 3 and left of 6
    - Bottom of 3 and bottom of 4
    - Left of 4 and bottom of 6
    - Right of 4 and left of 5
    """
    return [
        *zip(top_1, top_4[::-1], [1j]*size),
        *zip(bottom_1, top_2, [1j]*size),
        *zip(left_1, top_5, [1j]*size),
        *zip(right_1, right_6[::-1], [-1]*size),
        *zip(left_2, right_5, [-1]*size),
        *zip(right_2, top_6[::-1], [1j]*size),
        *zip(bottom_2, top_3, [1j]*size),
        *zip(left_3, bottom_5[::-1], [-1j]*size),
        *zip(right_3, left_6, [1]*size),
        *zip(bottom_3, bottom_4[::-1], [-1j]*size),
        *zip(left_4, bottom_6[::-1], [-1j]*size),
        *zip(right_4, left_5, [1]*size)
    ]


def gen_wrap_cube(grid, start_point, size=50):
    global edges_1, edges_2, edges_3, edges_4, edges_5, edges_6
    # I am not going to try to explain these comprehensions other than it was hell to write that took me an hour
    top_1 = [(p + start_point.real) + 0j for p in range(size)]
    left_1 = [start_point.real + p * 1j for p in range(size)]
    right_1 = [start_point.real + size-1 + p * 1j for p in range(size)]
    bottom_1 = [(p + start_point.real) + size * 1j-1j for p in range(size)]
    edges_1 = top_1 + left_1 + right_1 + bottom_1

    top_2 = [(p + start_point.real) + size * 1j for p in range(size)]
    left_2 = [start_point.real + (size + p) * 1j for p in range(size)]
    right_2 = [start_point.real + size-1 +
               (size + p) * 1j for p in range(size)]
    bottom_2 = [(p + start_point.real) + size * 2j-1j for p in range(size)]
    edges_2 = top_2 + left_2 + right_2 + bottom_2

    top_3 = [(p + start_point.real) + size * 2j for p in range(size)]
    left_3 = [start_point.real + (size*2 + p) * 1j for p in range(size)]
    right_3 = [start_point.real + size-1 +
               (size*2 + p) * 1j for p in range(size)]
    bottom_3 = [(p + start_point.real) + size * 3j-1j for p in range(size)]
    edges_3 = top_3 + left_3 + right_3 + bottom_3

    top_4 = [(p + start_point.real)+size + 0j for p in range(size)]
    left_4 = [start_point.real+size + p * 1j for p in range(size)]
    right_4 = [start_point.real+size + size-1 + p * 1j for p in range(size)]
    bottom_4 = [(p + start_point.real)+size +
                size * 1j-1j for p in range(size)]
    edges_4 = top_4 + left_4 + right_4 + bottom_4

    top_5 = [(p + start_point.real)-size + size * 2j for p in range(size)]
    left_5 = [start_point.real-size + (size*2 + p) * 1j for p in range(size)]
    right_5 = [start_point.real - 1 +
               (size*2 + p) * 1j for p in range(size)]
    bottom_5 = [(p + start_point.real)-size +
                size * 3j-1j for p in range(size)]
    edges_5 = top_5 + left_5 + right_5 + bottom_5

    top_6 = [(p + start_point.real)-size + size * 3j for p in range(size)]
    left_6 = [start_point.real-size + (size*3 + p) * 1j for p in range(size)]
    right_6 = [start_point.real - 1 +
               (size*3 + p) * 1j for p in range(size)]
    bottom_6 = [(p + start_point.real)-size +
                size * 4j-1j for p in range(size)]
    edges_6 = top_6 + left_6 + right_6 + bottom_6

    """
        1 4
        2
      5 3
      6
    Adjacent sides:
    - Top of 1 and left of 6
    - Bottom of 1 and top of 2
    - Left of 1 and left of 5
    - Right of 1 and left of 4
    - Left of 2 and top of 5
    - Right of 2 and bottom of 4
    - Bottom of 2 and top of 3
    - Left of 3 and right of 5
    - Right of 3 and right of 4
    - Bottom of 3 and right of 6
    - Top of 4 and bottom of 6
    - Bottom of 5 and top of 6
    """
    return [
        *zip(top_1, left_6, [1]*size),
        *zip(bottom_1, top_2, [1j]*size),
        *zip(left_1, left_5[::-1], [1]*size),
        *zip(right_1, left_4, [1]*size),
        *zip(left_2, top_5, [1j]*size),
        *zip(right_2, bottom_4, [-1j]*size),
        *zip(bottom_2, top_3, [1j]*size),
        *zip(left_3, right_5, [-1]*size),
        *zip(right_3, right_4[::-1], [-1]*size),
        *zip(bottom_3, right_6, [-1]*size),
        *zip(top_4, bottom_6, [-1j]*size),
        *zip(bottom_5, top_6, [1j]*size),
        *zip(left_6, top_1, [1j]*size),
        *zip(top_2, bottom_1, [-1j]*size),
        *zip(left_5, left_1[::-1], [1]*size),
        *zip(left_4, right_1, [-1]*size),
        *zip(top_5, left_2, [1]*size),
        *zip(bottom_4, right_2, [-1]*size),
        *zip(top_3, bottom_2, [-1j]*size),
        *zip(right_5, left_3, [1]*size),
        *zip(right_4, right_3[::-1], [-1]*size),
        *zip(right_6, bottom_3, [-1j]*size),
        *zip(bottom_6, top_4, [1j]*size),
        *zip(top_6, bottom_5, [-1j]*size),
    ]


def sign(n, real=True):
    if not real:
        return sign(n.imag)

    if n > 0:
        return 1
    elif n == 0:
        return 0
    else:
        return -1


def find_wrap(grid, point, dir):
    opposite_dir = -1 * dir
    while True:
        point += opposite_dir
        if point not in grid:
            return point + dir


def wrap_cube_example(wrap_pairs, point, dir):
    """
    Code for the example's shape
    """
    found = []
    for pair in wrap_pairs:
        if point in pair:
            found.append(
                (pair[1] if pair[0] == point else pair[0], pair[2] if pair[0] == point else -pair[2]))

    if len(found) == 1:
        return found[0]
    else:
        """
        - Up from 1 go to 4
        - Right from 1 go to 6
        - Left from 1 go to 5
        - Down from 1 go to 2
        - Up from 2 go to 1
        - Right from 2 go to 6
        - Left from 2 go to 5
        - Down from 2 go to 3
        - Up from 3 go to 2
        - Right from 3 go to 6
        - Left from 3 go to 5
        - Down from 3 go to 4
        - Up from 4 go to 1
        - Right from 4 go to 5
        - Left from 4 go to 6
        - Down from 4 go to 3
        - Up from 5 go to 1
        - Right from 5 go to 2
        - Left from 5 go to 4
        - Down from 5 go to 3
        - Up from 6 go to 2
        - Right from 6 go to 1
        - Left from 6 go to 3
        - Down from 6 go to 4
        """
        found_and_face = []
        for p in found:
            if p[0] in edges_1:
                found_and_face.append((p, 1))
            elif p[0] in edges_2:
                found_and_face.append((p, 2))
            elif p[0] in edges_3:
                found_and_face.append((p, 3))
            elif p[0] in edges_4:
                found_and_face.append((p, 4))
            elif p[0] in edges_5:
                found_and_face.append((p, 5))
            elif p[0] in edges_6:
                found_and_face.append((p, 6))
        if point in edges_1:
            for p in found_and_face:
                if p[1] == 4 and dir == -1j:
                    return p[0]
                elif p[1] == 6 and dir == 1:
                    return p[0]
                elif p[1] == 5 and dir == -1:
                    return p[0]
                elif p[1] == 2 and dir == 1j:
                    return p[0]
        elif point in edges_2:
            for p in found_and_face:
                if p[1] == 1 and dir == -1j:
                    return p[0]
                elif p[1] == 6 and dir == 1:
                    return p[0]
                elif p[1] == 5 and dir == -1:
                    return p[0]
                elif p[1] == 3 and dir == 1j:
                    return p[0]
        elif point in edges_3:
            for p in found_and_face:
                if p[1] == 2 and dir == -1j:
                    return p[0]
                elif p[1] == 6 and dir == 1:
                    return p[0]
                elif p[1] == 5 and dir == -1:
                    return p[0]
                elif p[1] == 4 and dir == 1j:
                    return p[0]
        elif point in edges_4:
            for p in found_and_face:
                if p[1] == 1 and dir == -1j:
                    return p[0]
                elif p[1] == 5 and dir == 1:
                    return p[0]
                elif p[1] == 6 and dir == -1:
                    return p[0]
                elif p[1] == 3 and dir == 1j:
                    return p[0]
        elif point in edges_5:
            for p in found_and_face:
                if p[1] == 1 and dir == -1j:
                    return p[0]
                elif p[1] == 2 and dir == 1:
                    return p[0]
                elif p[1] == 4 and dir == -1:
                    return p[0]
                elif p[1] == 3 and dir == 1j:
                    return p[0]
        elif point in edges_6:
            for p in found_and_face:
                if p[1] == 2 and dir == -1j:
                    return p[0]
                elif p[1] == 1 and dir == 1:
                    return p[0]
                elif p[1] == 3 and dir == -1:
                    return p[0]
                elif p[1] == 4 and dir == 1j:
                    return p[0]


def wrap_cube(wrap_pairs, point, dir):
    """
    Code for the example's shape
    """
    found = []
    for pair in wrap_pairs:
        if point == pair[0]:
            # print(pair[1] if pair[0] == point else pair[0], point)
            found.append(
                (pair[1] if pair[0] == point else pair[0], pair[2] if pair[0] == point else -pair[2]))
            # return pair[1] if pair[0] == point else pair[0]

    if len(found) == 1:
        return found[0]
    else:
        """
        - Up from 1 go to 6
        - Right from 1 go to 4
        - Left from 1 go to 5
        - Down from 1 go to 2
        - Up from 2 go to 1
        - Right from 2 go to 4
        - Left from 2 go to 5
        - Down from 2 go to 3
        - Up from 3 go to 2
        - Right from 3 go to 4
        - Left from 3 go to 5
        - Down from 3 go to 6
        - Up from 4 go to 6
        - Right from 4 go to 3
        - Left from 4 go to 1
        - Down from 4 go to 2
        - Up from 5 go to 2
        - Right from 5 go to 3
        - Left from 5 go to 1
        - Down from 5 go to 6
        - Up from 6 go to 5
        - Right from 6 go to 3
        - Left from 6 go to 1
        - Down from 6 go to 4
        """
        found_and_face = []
        for p in found:
            if p[0] in edges_1:
                found_and_face.append((p, 1))
            elif p[0] in edges_2:
                found_and_face.append((p, 2))
            elif p[0] in edges_3:
                found_and_face.append((p, 3))
            elif p[0] in edges_4:
                found_and_face.append((p, 4))
            elif p[0] in edges_5:
                found_and_face.append((p, 5))
            elif p[0] in edges_6:
                found_and_face.append((p, 6))
        if point in edges_1:
            for p in found_and_face:
                if p[1] == 6 and dir == -1j:
                    return p[0]
                elif p[1] == 4 and dir == 1:
                    return p[0]
                elif p[1] == 5 and dir == -1:
                    return p[0]
                elif p[1] == 2 and dir == 1j:
                    return p[0]
        elif point in edges_2:
            for p in found_and_face:
                if p[1] == 1 and dir == -1j:
                    return p[0]
                elif p[1] == 4 and dir == 1:
                    return p[0]
                elif p[1] == 5 and dir == -1:
                    return p[0]
                elif p[1] == 3 and dir == 1j:
                    return p[0]
        elif point in edges_3:
            for p in found_and_face:
                if p[1] == 2 and dir == -1j:
                    return p[0]
                elif p[1] == 4 and dir == 1:
                    return p[0]
                elif p[1] == 5 and dir == -1:
                    return p[0]
                elif p[1] == 6 and dir == 1j:
                    return p[0]
        elif point in edges_4:
            for p in found_and_face:
                if p[1] == 6 and dir == -1j:
                    return p[0]
                elif p[1] == 3 and dir == 1:
                    return p[0]
                elif p[1] == 1 and dir == -1:
                    return p[0]
                elif p[1] == 2 and dir == 1j:
                    return p[0]
        elif point in edges_5:
            for p in found_and_face:
                if p[1] == 2 and dir == -1j:
                    return p[0]
                elif p[1] == 3 and dir == 1:
                    return p[0]
                elif p[1] == 1 and dir == -1:
                    return p[0]
                elif p[1] == 6 and dir == 1j:
                    return p[0]
        elif point in edges_6:
            for p in found_and_face:
                if p[1] == 5 and dir == -1j:
                    return p[0]
                elif p[1] == 3 and dir == 1:
                    return p[0]
                elif p[1] == 1 and dir == -1:
                    return p[0]
                elif p[1] == 4 and dir == 1j:
                    return p[0]


def part_one(grid, start, instructions):
    current_point = start
    current_dir = 1
    for instruction in instructions:
        if abs(instruction.real) > 0:
            num = abs(int(instruction.real))
            current_dir = sign(instruction.real)
        else:
            num = abs(int(instruction.imag))
            current_dir = sign(instruction.imag) * 1j
        for _ in range(num):
            prev_point = current_point
            current_point += current_dir
            if current_point not in grid:
                current_point = find_wrap(grid, current_point, current_dir)

            if not grid[current_point]:
                current_point = prev_point
                break

    # Just in case we didn't bump into anything
    if current_dir == 1:
        facing = 0
    elif current_dir == 1j:
        facing = 1
    elif current_dir == -1:
        facing = 2
    elif current_dir == -1j:
        facing = 3
    return int(1000 * (current_point.imag + 1) + 4 * (current_point.real + 1) + facing)


def part_two(grid, start, instructions):
    current_point = start
    current_dir = 1
    wrap_pairs = gen_wrap_cube(grid, start, size=size)
    for i, instruction in enumerate(instructions):
        if isinstance(instruction, str):
            if instruction == "L":
                if current_dir == -1:
                    current_dir = 1j
                elif current_dir == 1j:
                    current_dir = 1
                elif current_dir == 1:
                    current_dir = -1j
                elif current_dir == -1j:
                    current_dir = -1
            elif instruction == "R":
                if current_dir == -1:
                    current_dir = -1j
                elif current_dir == -1j:
                    current_dir = 1
                elif current_dir == 1:
                    current_dir = 1j
                elif current_dir == 1j:
                    current_dir = -1
        else:
            for _ in range(int(instruction)):
                prev_point = current_point
                prev_dir = current_dir

                current_point += current_dir
                if current_point not in grid:
                    current_point, current_dir = wrap_cube(
                        wrap_pairs, prev_point, current_dir)

                if not grid[current_point]:
                    current_point = prev_point
                    current_dir = prev_dir
                    break

    if current_dir == 1:
        facing = 0
    elif current_dir == 1j:
        facing = 1
    elif current_dir == -1:
        facing = 2
    elif current_dir == -1j:
        facing = 3
    return int(1000 * (current_point.imag + 1) + 4 * (current_point.real + 1) + facing)


print(part_one(*get_input()))
print(part_two(*get_input(part_2=True)))
