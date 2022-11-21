def data():
    """1-4 m: mrfmmbjxr"""
    with open("input/2020/day_2", "r") as file:
        return [line.strip("\n") for line in file.readlines()]


def number_of(char, in_password):
    count = 0
    for letter in in_password:
        if letter == char:
            count += 1
    return count


def validate_pt1(line):
    split_line = line.split(" ")
    min_n, max_n = split_line[0].split("-")
    character = split_line[1].strip(":")
    password = split_line[2]

    occurrence = number_of(character, password)
    if occurrence >= int(min_n) and occurrence <= int(max_n):
        return True


def validate_pt2(line):
    split_line = line.split(" ")
    pos_1, pos_2 = split_line[0].split("-")
    character = split_line[1].strip(":")
    password = split_line[2]

    if (
        password[int(pos_1) - 1] == character
        and password[int(pos_2) - 1] != character
    ) or (
        password[int(pos_1) - 1] != character
        and password[int(pos_2) - 1] == character
    ):
        return True


def part_1():
    valid_passwords = 0
    for line in data():
        if validate_pt1(line):
            valid_passwords += 1

    print(valid_passwords)


def part_2():
    valid_passwords = 0
    for line in data():
        if validate_pt2(line):
            valid_passwords += 1

    print(valid_passwords)


part_1()
part_2()
