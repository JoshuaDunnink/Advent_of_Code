def get_sensors():
    with open("input/2022/day_15", "r") as file:
        sensors = []
        for line in file.readlines():
            append_line = []
            sens, beac = line.split(":")
            sensor = sens.split("at")[1].split(",")
            beacon = beac.split("at")[1].strip("\n").split(",")
            xys = []
            for xy in sensor:
                xys.append(int(xy.split("=")[1]))
            append_line.append(xys)
            xys = []
            for xy in beacon:
                xys.append(int(xy.split("=")[1]))
            append_line.append(xys)
            sensors.append(append_line)
    return sensors


def get_grid_and_aligned(sensors):
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0

    max_x_diff = 0
    max_y_diff = 0

    for sensor in sensors:
        for item in sensor:
            min_x = min_x if min_x < item[0] else item[0]
            max_x = max_x if max_x > item[0] else item[0]
            min_y = min_y if min_y > item[1] else item[1]
            max_y = max_y if max_y > item[1] else item[1]

        x_diff = abs(sensor[0][0]) - abs(sensor[1][0])
        y_diff = abs(sensor[0][1]) - abs(sensor[1][1])
        inv_x_diff = abs(sensor[1][0]) - abs(sensor[0][0])
        inv_y_diff = abs(sensor[1][1]) - abs(sensor[0][1])

        max_x_diff = x_diff if x_diff > max_x_diff else max_x_diff
        max_x_diff = inv_x_diff if inv_x_diff > max_x_diff else max_x_diff
        max_y_diff = y_diff if y_diff > max_y_diff else max_y_diff
        max_y_diff = inv_y_diff if inv_y_diff > max_y_diff else max_y_diff

    max_diff = max_y_diff if max_y_diff > max_x_diff else max_x_diff
    max_coord = max_y if max_y > max_x else max_x
    offset = max_diff + max_coord
    buffer = (max_diff + max_coord) * 2

    for sensor in sensors:
        sensor[0][0] = sensor[0][0] + offset
        sensor[1][0] = sensor[1][0] + offset
        sensor[0][1] = sensor[0][1] + offset
        sensor[1][1] = sensor[1][1] + offset

    grid = [
        ["." for _ in range(0, max_coord + buffer)]
        for _ in range(0, max_coord + buffer)
    ]

    for sensor in sensors:
        grid[sensor[0][1]][sensor[0][0]] = "S"
        grid[sensor[1][1]][sensor[1][0]] = "B"

    return grid, sensors, offset


def sensor_coverage(grid, sensors):
    for sensor in sensors:
        x_diff = sensor[0][0] - sensor[1][0]
        y_diff = sensor[0][1] - sensor[1][1]
        sensor_range = abs(x_diff) + abs(y_diff)
        for x in range(
            sensor[0][0] - sensor_range, sensor[0][0] + sensor_range + 1
        ):
            grid[sensor[0][1]][x] = (
                "#" if grid[sensor[0][1]][x] == "." else grid[sensor[0][1]][x]
            )
            for y in range(
                sensor[0][1] - sensor_range, sensor[0][1] + sensor_range + 1
            ):
                diff = abs(sensor[0][0] - x) + abs(sensor[0][1] - y)
                if diff <= sensor_range:
                    grid[y][x] = "#" if grid[y][x] == "." else grid[y][x]

    return grid


def get_count(grid, y):
    count = 0
    for char in grid[y]:
        if char == "#":
            count += 1
    return count


def print_example_only():
    sensors = get_sensors()
    grid, sensors, offset = get_grid_and_aligned(sensors)
    grid = sensor_coverage(grid, sensors)
    count = get_count(grid, 10 + offset)

    [print("".join(line)) for line in grid]
    print(count)


# print_example_only()

# better method:
# determine sensor ranges that cross target y
# determine distance from y with sensor to determine actual coverage
# create set of coverage to rule out double coverage


def determine_target_sensors(sensors, target_y):
    target_sensors = []
    for sensor, beacon in sensors:
        sensor_range = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        if (sensor[1] > target_y and sensor[1] - sensor_range < target_y) or (
            sensor[1] < target_y and sensor[1] + sensor_range > target_y
        ):
            delta = abs(sensor[1] - target_y)
            target_sensors.append([sensor[0], sensor_range, delta])
    return target_sensors


def determine_coverage(target_sensors):
    line_coverage = set()
    for sensor, sensor_range, delta in target_sensors:
        for x in range(
            (sensor - (sensor_range - delta)),
            (sensor + (sensor_range - delta)),
        ):
            line_coverage.add((x))
    return line_coverage


def smart_part_1():
    target_y = 2000000
    sensors = get_sensors()
    target_sensors = determine_target_sensors(sensors, target_y)
    coverage = determine_coverage(target_sensors)
    print(len(coverage))


smart_part_1()
