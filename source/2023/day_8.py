from math import lcm

def data():
    with open("input/2023/day_8", "r") as file:
        return file.readlines()


instructions, *raw_coordinates = [line.strip() for line in data() if line.strip()]

coordinates = {}
for coordinate in raw_coordinates:
    key, waypoints = [item.strip() for item in coordinate.split("=")]
    left, right = [point.strip().strip("()") for point in waypoints.split(",")]
    coordinates.update({key: (left, right)})


def walk_from_AAA_to_ZZZ(current_location, finish):
    steps = 0
    while not current_location == finish:
        for instruction in instructions:
            pointer = 0 if instruction == "L" else 1
            current_location = coordinates.get(current_location)[pointer]
            steps += 1
            if current_location == finish:
                return steps


def walk_from_start_to_finishes(current_location, finishes):
    steps = 0
    while not current_location in finishes:
        for instruction in instructions:
            pointer = 0 if instruction == "L" else 1
            current_location = coordinates.get(current_location)[pointer]
            steps += 1
            if current_location in finishes:
                return steps


def part_1():
    current_location = "AAA"
    finish = "ZZZ"
    print(walk_from_AAA_to_ZZZ(current_location, finish))


def part_2():
    start_points = []
    finishes = []
    finishing_steps = []
    for key in coordinates.keys():
        if key[-1] == "A":
            start_points.append(key)
        if key[-1] == "Z":
            finishes.append(key)

    for start in start_points:
        finishing_steps.append(walk_from_start_to_finishes(start, finishes))

    print(lcm(*finishing_steps))


part_2()
