"""Lessons learned
dijkstras shortest (least effort) path algorithm
deque is optimised for leftpop
what is heapq?

"""


import string
from collections import deque


def get_grid():
    with open("input/2022/day_12", "r") as file:
        start = []
        end = []
        grid = []
        for row, line in enumerate(file.readlines()):
            grid.append(
                [
                    (int(string.ascii_lowercase.index(char)) + 1)
                    if char.islower()
                    else char
                    for char in line.strip("\n")
                ]
            )
            for column, char in enumerate(grid[row]):
                if char == "S":
                    start = (row, column)
                    grid[row][column] = 1
                elif char == "E":
                    end = (row, column)
                    grid[row][column] = 26
        return start, end, grid


def get_shortest_path(start: tuple, end: tuple, grid: list[list[int, str]]):
    boundaries = (len(grid) - 1, len(grid[0]) - 1)
    options = deque()
    options.append((0, start[0], start[1]))

    visited = set()
    while options:
        step, y, x = options.popleft()
        if (y, x) in visited:
            continue
        visited.add((y, x))
        if (y, x) == end:
            return step
        else:
            for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_y, new_x = y + dy, x + dx
                if (
                    0 <= new_y < boundaries[0]
                    and 0 <= new_x < boundaries[1]
                    and (grid[new_y][new_x] - grid[y][x]) <= 1
                ):
                    options.append((step + 1, new_y, new_x))
    return 999


start, end, grid = get_grid()
starting_points = []
for n_row, row in enumerate(grid):
    for n_column, value in enumerate(row):
        if value == 1:
            starting_points.append(
                get_shortest_path((n_row, n_column), end, grid)
            )

print("part_1: " + str(get_shortest_path(start, end, grid)))
print("part_2: " + str(min(starting_points)))
