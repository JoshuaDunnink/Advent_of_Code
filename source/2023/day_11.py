import numpy as np
from itertools import permutations


def data():
    with open("input/2023/day_11", "r") as file:
        file_data = file.readlines()
        lines = []
        for line in file_data:
            lines.append([char for char in line.strip()])
        return lines


def find_expansion_lines(universe):
    expansion_lines = []
    for index, line in enumerate(universe):
        if "#" not in "".join(line):
            expansion_lines.append(index)
    return expansion_lines


def get_expansion_lines(universe):
    y = find_expansion_lines(universe)
    x = find_expansion_lines(np.array(universe).transpose())
    return y, x


def find_galaxy_coordinates(universe):
    galaxy_map = set()
    for y, line in enumerate(universe):
        for x, char in enumerate(line):
            if char == "#":
                galaxy_map.add((y, x))
    return galaxy_map


def expand_map(expansion_lines, galaxy_map, factor):
    factor -= 1
    expanded_map = []
    for y, x in galaxy_map:
        new_y = y
        new_x = x
        for line in expansion_lines[0]:
            if line < y:
                new_y += factor
        for line in expansion_lines[1]:
            if line < x:
                new_x += factor
        expanded_map.append((new_y, new_x))
    return expanded_map


def calculate(factor):
    universe = data()
    galaxy_map = find_galaxy_coordinates(universe)
    expansion_lines = get_expansion_lines(universe)
    new_map = expand_map(expansion_lines, galaxy_map, factor)
    galaxy_permutations = permutations(list(new_map), 2)
    steps = 0
    done = set()

    for start, end in galaxy_permutations:
        if (end, start) not in done:
            path = abs((start[0] - end[0])) + abs((start[1] - end[1]))
            done.add((start, end))
            steps += path
    return steps


def main():
    print(f"part 1: {calculate(2)}")
    print(f"part 2: {calculate(1_000_000)}")


main()
