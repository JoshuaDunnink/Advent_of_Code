def data():
    with open("input/2023/day_10_tst", "r") as file:
        file_data = file.readlines()
        lines = []
        for line in file_data:
            lines.append([char for char in line.strip()])
        return lines


current_char = "S"
x = 1
y = 0


def next_step(previous, location, char):
    right = 0, 1
    left = 0, -1
    up = -1, 0
    down = 1, 0
    if char == "|":
        if location[y] - previous[y] == 1:
            return down
        else:
            return up
    if char == "-":
        if location[x] - previous[x] == 1:
            return right
        else:
            return left
    if char == "L":
        if location[y] - previous[y] == 1:
            return right
        else:
            return up
    if char == "J":
        if location[y] - previous[y] == 1:
            return left
        else:
            return up
    if char == "7":
        if location[y] - previous[y] == -1:
            return left
        else:
            return down
    if char == "F":
        if location[y] - previous[y] == -1:
            return right
        else:
            return down


def get_starting_location(grid):
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == "S":
                return y, x


def mark_path(grid, previous):
    grid[previous[y]][previous[x]] = "X"
    return grid


# def count_included_cels(line: list):
#     locations = []
#     if line.count("X") >= 2:
#         for index, char in enumerate(line):
#             if char == "X":
#                 locations.append(index)

#         count = 0
#         for start, end in zip(locations[::2], locations[1::2]):
#             count += end - start - 1
#         return count
#     return 0


def main():
    grid = data()
    previous = get_starting_location(grid)
    current = (previous[y], previous[x] + 1)
    char = grid[current[y]][current[x]]
    steps = 1
    grid = mark_path(grid, previous)

    while char != "X":
        next = next_step(previous, current, char)
        previous = current
        current = (current[y] + next[y], current[x] + next[x])
        char = grid[current[y]][current[x]]
        steps += 1
        grid = mark_path(grid, previous)

    count = 0
    # for index, line in enumerate(grid):
    #     print(index)
    #     count += count_included_cels(line)

    print("part 1: " + str(int(steps / 2)))
    print("part 2: " + str(count))


main()
