"""
How can I make this faster?
"""


def get_rock_map():
    with open("input/2022/day_14", "r") as file:
        x = 0
        y = 1
        rocks = []
        for line in file.readlines():
            rocks.append(
                [
                    [int(x) for x in item.split(",")]
                    for item in line.strip("\n").split(" -> ")
                ]
            )

        max_x, max_y, min_x, min_y = 0, 0, 0, 0
        for line in rocks:
            for coordinate in line:
                max_x = coordinate[x] if coordinate[x] > max_x else max_x
                max_y = coordinate[y] if coordinate[y] > max_y else max_y
                min_x = coordinate[x] if coordinate[x] < max_x else min_x
                min_y = coordinate[y] if coordinate[y] < max_y else min_y

        buffer = 200
        x_min_offset = min_x - buffer
        x_max_offset = max_x + (buffer * 2) - min_x
        for line in rocks:
            for rock in line:
                rock[0] = rock[0] - x_min_offset

        drop_point = [0, 500 - x_min_offset]

        rock_map = [
            [" " for _ in range(0, x_max_offset)] for _ in range(0, max_y + 5)
        ]
        for line in rocks:
            previous_rock = []
            for rock in line:
                if not previous_rock:
                    previous_rock = rock
                elif previous_rock:
                    if (dx := rock[x] - previous_rock[x]) > 0:
                        for dx in range(previous_rock[x], rock[x] + 1):
                            rock_map[rock[y]][dx] = "#"
                    elif dx < 0:
                        for dx in range(rock[x], previous_rock[x] + 1):
                            rock_map[rock[y]][dx] = "#"

                    elif (dy := rock[y] - previous_rock[y]) > 0:
                        for dy in range(previous_rock[y], rock[y] + 1):
                            rock_map[dy][rock[x]] = "#"
                    elif dy < 0:
                        for dy in range(rock[y], previous_rock[y] + 1):
                            rock_map[dy][rock[x]] = "#"
                    previous_rock = rock
        rock_map[drop_point[0]][drop_point[1]] = "+"

        floor_level = max_y + 2

        return rock_map, drop_point, floor_level


def drop_particle(sand_map, drop_point, p1=True):
    directions = (1, 0), (1, -1), (1, 1)

    current_location = drop_point

    reached_top = False
    resting = False
    reached_bottom = False
    while not resting or (not p1 and not reached_top):
        if current_location[0] != len(sand_map) - 1:
            reached_bottom = False
            available_direction = []
            for direction in directions:
                if (
                    sand_map[current_location[0] + direction[0]][
                        current_location[1] + direction[1]
                    ]
                    == " "
                ):
                    available_direction.append(True)
                else:
                    available_direction.append(False)

            for index, option in enumerate(available_direction):
                if option:
                    current_location = (
                        current_location[0] + directions[index][0],
                        current_location[1] + directions[index][1],
                    )
                    break

            if all([not option for option in available_direction]):
                resting = True
                if current_location == drop_point:
                    reached_top = True
                    resting = True
                break
        elif current_location[0] == len(sand_map) - 1:
            resting = True
            reached_bottom = True

    sand_map[current_location[0]][current_location[1]] = "o"
    return sand_map, any([reached_bottom, reached_top])


def part_1():
    rock_map, drop_point, _ = get_rock_map()
    reached_bottom = False
    sand = 0
    while not reached_bottom:
        rock_map, reached_bottom = drop_particle(rock_map, drop_point)
        sand += 1

    # [print("".join(line)) for line in rock_map]
    print("part_1: " + str(sand - 1))


def part_2():
    rock_map, drop_point, floor_level = get_rock_map()
    for i, _ in enumerate(rock_map[floor_level]):
        rock_map[floor_level][i] = "#"
    reached_top = False
    sand = 0
    while not reached_top:
        rock_map, reached_top = drop_particle(rock_map, drop_point, False)
        sand += 1

    # [print("".join(line)) for line in rock_map]
    print("part_2: " + str(sand))


part_1()
part_2()
