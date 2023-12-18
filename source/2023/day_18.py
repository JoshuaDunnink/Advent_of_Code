import re
import numpy as np

from helpers import timing


def data():
    with open("input/2023/day_18", "r") as file:
        data = [line.strip().split(" ") for line in file.read().split("\n")]
        return [(x, int(y), z) for x, y, z in data]


def get_instructions():
    instructions = data()
    right = 5
    down = 5
    for line in instructions:
        if line[0] == "R":
            right += line[1]
        if line[0] == "D":
            down += line[1]
    return instructions


def mark_grid(grid, dig_range, direction, location, x=False, y=False):
    point = []
    if x:
        for _ in range(dig_range):
            location[1] += 1 * direction
            grid[location[0]][location[1]] = "#"
            loca = (location[0], location[1])
            point.append(loca)
    if y:
        for _ in range(dig_range):
            location[0] += 1 * direction
            grid[location[0]][location[1]] = "#"
            loca = (location[0], location[1])
            point.append(loca)
    return grid, location, point


def count_digged(grid):
    dig_count = 0
    for line in grid:
        first = True
        for match in re.finditer("#", "".join(line)):
            if first:
                first_hash = match
                first = False
            else:
                last = match
        if last:
            dig_count += last.end() - first_hash.start()
        else:
            dig_count += first_hash.end() - first_hash.start()
    return dig_count


def polygon_area(vertices):
    """
    Return the area of the polygon enclosed by vertices using the shoelace
    algorithm.
    """
    a = np.vstack((vertices, vertices[0]))
    S1 = sum(a[:-1, 0] * a[1:, 1])
    S2 = sum(a[:-1, 1] * a[1:, 0])
    return abs(S1 - S2) / 2


def polygon_area2(corners):
    """
    source: 
    https://code.activestate.com/recipes/578047-area-of-polygon-using-shoelace-formula/
    """
    n = len(corners)  # of corners
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2
    return area


def polygon_perimiter(instructions):
    """picks theorem but +1 instead of -1????
    source:
    https://scipython.com/book/chapter-6-numpy/problems/p61/the-shoelace-algorithm/
    """
    return sum([len for _, len, _ in instructions]) / 2 + 1


def get_points(instructions):
    y, x = 0, 0
    directions = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}
    points = [(y, x)]
    for direction, instruction_range, _ in instructions:
        dir_y, dir_x = directions[direction]
        y += dir_y * instruction_range
        x += dir_x * instruction_range
        points.append((y, x))
    return points


def transform_into_instructions(instructions):
    transformed = []
    directions = {0: "R", 1: "D", 2: "L", 3: "U"}
    for line in instructions:
        transformed.append((directions[int(line[2][7])], int(line[2][2:7], 16), None))
    return transformed


@timing
def part_1():
    instructions = get_instructions()
    points = get_points(instructions)
    area = polygon_area(points) + polygon_perimiter(instructions)
    print(f"part_1: {area}")


@timing
def part_2():
    instructions = get_instructions()
    transformed = transform_into_instructions(instructions)
    points = get_points(transformed)
    area = polygon_area(points) + polygon_perimiter(transformed)
    print(f"part_2: {area}")


part_1()
part_2()
