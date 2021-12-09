def read_input():
    with open("input/day_2") as movement:
        results = movement.readlines()
    return results


def move1():
    horizontal = 0
    depth = 0
    for line in read_input():
        action = line.split()
        match action[0]:
            case "forward":
                horizontal += int(action[1])
            case "up":
                depth -= int(action[1])
            case "down":
                depth += int(action[1])
            case _:
                print(action[0])
    final = horizontal * depth
    print(final)


def move2():
    horizontal = 0
    depth = 0
    aim = 0
    for line in read_input():
        action = line.split()
        match action[0]:
            case "forward":
                horizontal += int(action[1])
                depth += int(action[1]) * aim
            case "up":
                aim -= int(action[1])
            case "down":
                aim += int(action[1])
            case _:
                print(action[0])
    final = horizontal * depth
    print(final)


move1()
move2()
