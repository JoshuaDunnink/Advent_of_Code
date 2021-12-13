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
    return max_data+1


def create_grid(size):
    return np.zeros((size, size), dtype=np.int32)


def mark_lines(data, grid):
    """[x1, y1, x2, y2]"""
    for coordinates in data:
        y2 = coordinates[0]
        y1 = coordinates[2]
        x2 = coordinates[1]
        x1 = coordinates[3]

        if x1 == x2:
            if y1 <= y2:
                for y in range(y1, y2+1):
                    grid[x1][y] += 1
            elif y1 >= y2:
                for y in range(y2, y1+1):
                    grid[x1][y] += 1

        elif y1 == y2:
            if x1 <= x2:
                for x in range(x1, x2+1):
                    grid[x][y1] += 1
            elif x1 >= x2:
                for x in range(x2, x1+1):
                    grid[x][y1] += 1

        # if y1 != y2 and x1 != x2:
        #     if x1 < x2 and y1 < y2:
        #         x = x1+1
        #         for y in range(y1, y2+1):
        #             grid[-x-1][-y] += 1
        #             x += 1

        #     elif x1 > x2 and y1 > y2:
        #         x = x2+1
        #         for y in range(y2, y1+1):
        #             grid[-x-1][y] += 1
        #             x += 1

        # if x1 < x2 and y1 > y2:
        #     x = x1+1
        #     for y in range(y1, y2+1):
        #         grid[x][y] += 1
        #         x += 1

        # elif x1 > x2 and y1 < y2:
        #     x = x2+1
        #     for y in range(y1, y2):
        #         grid[x-1][y] += 1
        #         x += 1



    return grid


def count_overlap(grid):
    return len(np.where(grid >= 2)[0])


data = get_input()
grid = create_grid(get_grid_size(data))
marked_grid = mark_lines(data, grid)
print(marked_grid)
print(count_overlap(marked_grid))
