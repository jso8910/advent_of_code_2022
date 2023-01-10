from collections import defaultdict


def get_input():
    with open("day_15/input.txt", "r") as f:
        file = f.read().splitlines()

    sensors = []
    for line in file:
        coords = list(map(int, [t.split("=")[1]
                      for t in line.replace(":", ",").split(",")]))
        sensors.append(
            {"sensor": coords[0] + coords[1]*1j, "beacon": coords[2]+coords[3]*1j})

    return sensors


def manhattan_distance(p1, p2):
    return abs(p2.real - p1.real) + abs(p2.imag - p1.imag)


def part_one(sensors):
    y = 2_000_000
    vals = set()
    beacons = [sensor["beacon"] for sensor in sensors]
    for sensor in sensors:
        dist = manhattan_distance(sensor["sensor"], sensor["beacon"])
        vals = vals | {col for col in range(int(sensor["sensor"].real - dist), int(
            sensor["sensor"].real + dist + 1)) if manhattan_distance(sensor["sensor"], col + y*1j) <= dist and col + y*1j not in beacons}

    return len(vals)


def part_two(sensors):
    MAX_XY = 4_000_000
    perimeter_points = defaultdict(int)
    for sensor in sensors:
        # We want to find the points outside the perimeter
        dist = manhattan_distance(sensor["sensor"], sensor["beacon"]) + 1
        for p in range(int(dist)):
            point_upper_right = sensor["sensor"] + (dist - p) - p*1j
            point_upper_left = sensor["sensor"] - (dist - p) - p*1j
            point_bottom_right = sensor["sensor"] + (dist - p) + p*1j
            point_bottom_left = sensor["sensor"] - (dist - p) + p*1j

            if 0 <= point_upper_right.real <= MAX_XY and 0 <= point_upper_right.imag <= MAX_XY:
                perimeter_points[point_upper_right] += 1
            if 0 <= point_upper_left.real <= MAX_XY and 0 <= point_upper_left.imag <= MAX_XY:
                perimeter_points[point_upper_left] += 1
            if 0 <= point_bottom_right.real <= MAX_XY and 0 <= point_bottom_right.imag <= MAX_XY:
                perimeter_points[point_bottom_right] += 1
            if 0 <= point_bottom_left.real <= MAX_XY and 0 <= point_bottom_left.imag <= MAX_XY:
                perimeter_points[point_bottom_left] += 1

    for point in sorted(perimeter_points, reverse=True, key=lambda x: perimeter_points[x]):
        point_in_sensor = False
        for sensor in sensors:
            dist = manhattan_distance(sensor["sensor"], sensor["beacon"])
            if manhattan_distance(sensor["sensor"], point) <= dist:
                point_in_sensor = True
                break
        if not point_in_sensor:
            return int(point.real * MAX_XY + point.imag)


print(part_one(get_input()))
print(part_two(get_input()))
