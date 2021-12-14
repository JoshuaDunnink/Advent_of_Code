import numpy as np


def get_input():
    with open("input/example_day_5", "r") as file:
        raw_data = [
            line.strip("\n").replace("->", ",").split(",") for line in file
        ]
    return [list(map(int, line)) for line in raw_data]


def get_grid_size(data):
    max_data = 0
    for line in data:
        if (max_point := max(line)) > max_data:
            max_data = max_point
    return max_data + 1


def create_grid(size):
    return np.zeros((size, size), dtype=np.int32)


def mark_lines(data, grid):
    """[x1, y1, x2, y2]"""
    for coordinates in data:
        x1 = coordinates[0]
        y1 = coordinates[1]
        x2 = coordinates[2]
        y2 = coordinates[3]

    if x1 == x2:
        grid[y1][x1] += 1
        grid[y2][x2] += 1
        y = y1 - y2
        if y > 1:
            for i in range(1, abs(y)):
                grid[y1 - i][x1] += 1
        else:
            for i in range(1, abs(y)):
                grid[y1 + i][x1] += 1
    if y1 == y2:
        grid[y1][x1] += 1
        grid[y2][x2] += 1
        x = x1 - x2
        if x > 0:
            for i in range(1, abs(x)):
                grid[y2][x2 + i] += 1
        else:
            for i in range(1, abs(x)):
                grid[y2][x2 - i] += 1
    if x1 > x2 and y1 > y2:
        grid[y1][x1] += 1
        grid[y2][x2] += 1
        x = x1 - x2
        y = y1 - y2
        if abs(x) > abs(y):
            for i in range(1, abs(x)):
                grid[y1 - i][x1 - i] += 1
        else:
            for i in range(1, abs(y)):
                grid[y1 - i][x1 - i] += 1
    if x1 < x2 and y1 < y2:
        grid[y1][x1] += 1
        grid[y2][x2] += 1
        x = x1 - x2
        y = y2 - y1
        if abs(x) > abs(y):
            for i in range(1, abs(x)):
                grid[y1 + i][x1 + i] += 1
        else:
            for i in range(1, abs(y)):
                grid[y1 + i][x1 + i] += 1
    if x1 > x2 and y1 < y2:
        grid[y1][x1] += 1
        grid[y2][x2] += 1
        x = x1 - x2
        y = y1 - y2
        if abs(x) > abs(y):
            for i in range(1, abs(x)):
                grid[y1 + i][x1 - i] += 1
        else:
            for i in range(1, abs(y)):
                grid[y1 + i][x1 - i] += 1
    if x1 < x2 and y1 > y2:
        grid[y1][x1] += 1
        grid[y2][x2] += 1
        x = x1 - x2
        y = y2 - y1
        if abs(x) > abs(y):
            for i in range(1, abs(x)):
                grid[y1 - i][x1 + i] += 1
        else:
            for i in range(1, abs(y)):
                grid[y1 - i][x1 + i] += 1
    print(grid)
    return grid


def count_overlap(grid):
    return len(np.where(grid >= 2)[0])


data = get_input()
grid = create_grid(get_grid_size(data))
marked_grid = mark_lines(data, grid)
print(marked_grid)
print(count_overlap(marked_grid))
